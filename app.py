from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv
import json
import requests
from urllib.parse import quote
import threading
import webbrowser

load_dotenv()

app = Flask(__name__)

# Configuração do Banco de Dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orcamento.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ========== MODELOS DO BANCO DE DADOS ==========
class TipoTrabalho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    descricao = db.Column(db.String(255))
    criado_em = db.Column(db.DateTime, default=datetime.now)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'criado_em': self.criado_em.strftime('%d/%m/%Y %H:%M:%S')
        }


class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    descricao = db.Column(db.String(255))
    criado_em = db.Column(db.DateTime, default=datetime.now)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'criado_em': self.criado_em.strftime('%d/%m/%Y %H:%M:%S')
        }

# Criar tabelas
with app.app_context():
    db.create_all()

# Configurações para WhatsApp via pywhatkit
# Número alvo para receber os orçamentos
WHATSAPP_PHONE = os.getenv('WHATSAPP_PHONE', '+5519997328677')  # Formato com + para pywhatkit


def formatar_mensagem_whatsapp(dados):
    """Formata os dados do orçamento em uma mensagem formatada para WhatsApp"""
    
    # Fase 1
    mensagem = f"""
🎯 *NOVO ORÇAMENTO* 🎯

📋 *INFORMAÇÕES DO CLIENTE*
━━━━━━━━━━━━━━━━━━━━━━━━
👤 Nome: {dados.get('nome_cliente', '')}
📱 Contato: {dados.get('contato', '')}
📍 CEP: {dados.get('cep', '')}
🏠 Endereço: {dados.get('endereco', '')}
🔢 Número: {dados.get('numero', '')}
ℹ️ Complemento: {dados.get('complemento', 'N/A')}
📅 Data de Fechamento: {dados.get('data_fechamento', '')}

📦 *DETALHES DO TRABALHO*
━━━━━━━━━━━━━━━━━━━━━━━━
🔧 Tipo de Trabalho: {dados.get('tipo_trabalho', '')}
🛠️ Materiais: {dados.get('materiais', '')}
📐 Quantidade: {dados.get('quantidade', '')}
📏 Medidas: {dados.get('medidas', '')}
🔨 Instalação: {dados.get('instalacao', 'Não informado')}

⏰ Enviado em: {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}
"""
    
    return mensagem


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


# ========== ROTAS DA API - TIPOS DE TRABALHO ==========
@app.route('/api/tipos-trabalho', methods=['GET'])
def get_tipos_trabalho():
    tipos = TipoTrabalho.query.all()
    return jsonify([t.to_dict() for t in tipos])


@app.route('/api/tipos-trabalho', methods=['POST'])
def criar_tipo_trabalho():
    try:
        dados = request.json
        novo_tipo = TipoTrabalho(
            nome=dados.get('nome'),
            descricao=dados.get('descricao', '')
        )
        db.session.add(novo_tipo)
        db.session.commit()
        return jsonify({'success': True, 'data': novo_tipo.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/api/tipos-trabalho/<int:id>', methods=['PUT'])
def atualizar_tipo_trabalho(id):
    try:
        tipo = TipoTrabalho.query.get_or_404(id)
        dados = request.json
        tipo.nome = dados.get('nome', tipo.nome)
        tipo.descricao = dados.get('descricao', tipo.descricao)
        db.session.commit()
        return jsonify({'success': True, 'data': tipo.to_dict()})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/api/tipos-trabalho/<int:id>', methods=['DELETE'])
def deletar_tipo_trabalho(id):
    try:
        tipo = TipoTrabalho.query.get_or_404(id)
        db.session.delete(tipo)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Deletado com sucesso'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 400


# ========== ROTAS DA API - MATERIAIS ==========
@app.route('/api/materiais', methods=['GET'])
def get_materiais():
    materiais = Material.query.all()
    return jsonify([m.to_dict() for m in materiais])


@app.route('/api/materiais', methods=['POST'])
def criar_material():
    try:
        dados = request.json
        novo_material = Material(
            nome=dados.get('nome'),
            descricao=dados.get('descricao', '')
        )
        db.session.add(novo_material)
        db.session.commit()
        return jsonify({'success': True, 'data': novo_material.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/api/materiais/<int:id>', methods=['PUT'])
def atualizar_material(id):
    try:
        material = Material.query.get_or_404(id)
        dados = request.json
        material.nome = dados.get('nome', material.nome)
        material.descricao = dados.get('descricao', material.descricao)
        db.session.commit()
        return jsonify({'success': True, 'data': material.to_dict()})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/api/materiais/<int:id>', methods=['DELETE'])
def deletar_material(id):
    try:
        material = Material.query.get_or_404(id)
        db.session.delete(material)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Deletado com sucesso'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/api/enviar-orcamento', methods=['POST'])
def enviar_orcamento():
    try:
        dados = request.json
        
        # Validar dados obrigatórios
        campos_obrigatorios = [
            'nome_cliente', 'contato', 'cep', 'endereco', 
            'numero', 'data_fechamento', 'tipo_trabalho', 
            'materiais', 'quantidade', 'medidas', 'instalacao'
        ]
        
        for campo in campos_obrigatorios:
            if not dados.get(campo):
                return jsonify({'success': False, 'error': f'Campo obrigatório faltando: {campo}'}), 400
        
        # Formatar mensagem
        mensagem = formatar_mensagem_whatsapp(dados)
        
        # Enviar via WhatsApp Web URL (abre o navegador)
        def enviar_whatsapp():
            try:
                print(f"🚀 Iniciando envio para {WHATSAPP_PHONE}")
                
                # Criar URL do WhatsApp com a mensagem
                # Formato: https://web.whatsapp.com/send?phone=NUMERO&text=MENSAGEM
                mensagem_encoded = quote(mensagem)
                whatsapp_url = f"https://web.whatsapp.com/send?phone={WHATSAPP_PHONE.replace('+', '')}&text={mensagem_encoded}"
                
                # Abrir no navegador padrão
                webbrowser.open(whatsapp_url)
                print(f"✅ Janela WhatsApp Web aberta para {WHATSAPP_PHONE}")
            except Exception as e:
                print(f"❌ Erro ao abrir WhatsApp: {str(e)}")
        
        # Iniciar thread de envio (não bloqueia o servidor)
        thread = threading.Thread(target=enviar_whatsapp, daemon=True)
        thread.start()
        
        # Retornar resposta imediatamente
        return jsonify({
            'success': True,
            'message': f'✅ Abrindo WhatsApp Web para enviar orçamento!',
            'note': 'Seu navegador será aberto. Clique em "Enviar" para confirmar a mensagem.',
            'timestamp': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/validar-cep/<cep>', methods=['GET'])
def validar_cep(cep):
    """Valida CEP e tenta buscar informações (opcional)"""
    try:
        import requests
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        
        if response.status_code == 200:
            data = response.json()
            if 'erro' not in data:
                return jsonify({
                    'success': True,
                    'endereco': data.get('logradouro', ''),
                    'bairro': data.get('bairro', ''),
                    'cidade': data.get('localidade', ''),
                    'estado': data.get('uf', '')
                }), 200
        
        return jsonify({'success': False, 'error': 'CEP não encontrado'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV', 'development') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
