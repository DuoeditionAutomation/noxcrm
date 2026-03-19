"""
Script de teste para o Sistema de Orçamento VivaCRM

Use este script para:
1. Testar a formatação de mensagens
2. Validar dados
3. Testar sem dependências do servidor Flask
"""

import json
from datetime import datetime

def formatar_mensagem_whatsapp(dados):
    """Formata os dados do orçamento em uma mensagem formatada para WhatsApp"""
    
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


def teste_basico():
    """Teste básico com dados de exemplo"""
    print("=" * 60)
    print("TESTE 1: Formatação de Mensagem Básica")
    print("=" * 60)
    
    dados_teste = {
        'nome_cliente': 'João da Silva',
        'contato': '(11) 98765-4321',
        'cep': '01310-100',
        'endereco': 'Avenida Paulista',
        'numero': '1000',
        'complemento': 'Apartamento 1201',
        'data_fechamento': '2026-04-15',
        'tipo_trabalho': 'Instalação de Persianas',
        'materiais': 'Alumínio, Vidro',
        'quantidade': '3',
        'medidas': '100cm x 150cm | 80cm x 120cm',
        'instalacao': 'Sim'
    }
    
    mensagem = formatar_mensagem_whatsapp(dados_teste)
    print(mensagem)
    
    return True


def teste_com_espacos():
    """Teste com dados que têm espaços"""
    print("\n" + "=" * 60)
    print("TESTE 2: Dados com Espaços e Caracteres Especiais")
    print("=" * 60)
    
    dados_teste = {
        'nome_cliente': 'Maria José da & Silva',
        'contato': '(21) 99876-5432',
        'cep': '20000-000',
        'endereco': 'Rua das Flores - Centro',
        'numero': '555',
        'complemento': 'Sala 101 - Fundos',
        'data_fechamento': '2026-05-20',
        'tipo_trabalho': 'Cortinas & Revestimento',
        'materiais': 'Alumínio, PVC, Madeira',
        'quantidade': '5',
        'medidas': '200cm x 180cm | 150cm x 200cm | 100cm x 250cm',
        'instalacao': 'Não'
    }
    
    mensagem = formatar_mensagem_whatsapp(dados_teste)
    print(mensagem)
    
    return True


def teste_dados_minimos():
    """Teste com apenas dados obrigatórios"""
    print("\n" + "=" * 60)
    print("TESTE 3: Apenas Dados Obrigatórios")
    print("=" * 60)
    
    dados_teste = {
        'nome_cliente': 'Pedro',
        'contato': '(11) 99999-9999',
        'cep': '12345-678',
        'endereco': 'Rua A',
        'numero': '123',
        'complemento': '',
        'data_fechamento': '2026-03-25',
        'tipo_trabalho': 'Vidros',
        'materiais': 'Vidro',
        'quantidade': '1',
        'medidas': '100cm x 200cm',
        'instalacao': 'Sim'
    }
    
    mensagem = formatar_mensagem_whatsapp(dados_teste)
    print(mensagem)
    
    return True


def teste_multiplas_medidas():
    """Teste com múltiplas medições"""
    print("\n" + "=" * 60)
    print("TESTE 4: Múltiplas Medições")
    print("=" * 60)
    
    dados_teste = {
        'nome_cliente': 'Empresa XYZ Ltda',
        'contato': '(85) 99888-7777',
        'cep': '60000-000',
        'endereco': 'Av. Industrial',
        'numero': '2000',
        'complemento': 'Galpão 5',
        'data_fechamento': '2026-06-10',
        'tipo_trabalho': 'Divisórias',
        'materiais': 'Alumínio, Vidro',
        'quantidade': '10',
        'medidas': '300cm x 400cm | 250cm x 350cm | 200cm x 300cm | 150cm x 250cm | 100cm x 150cm',
        'instalacao': 'Sim'
    }
    
    mensagem = formatar_mensagem_whatsapp(dados_teste)
    print(mensagem)
    
    return True


def teste_validacao():
    """Teste de validação de campos"""
    print("\n" + "=" * 60)
    print("TESTE 5: Validação de Campos")
    print("=" * 60)
    
    campos_obrigatorios = [
        'nome_cliente', 'contato', 'cep', 'endereco',
        'numero', 'data_fechamento', 'tipo_trabalho',
        'materiais', 'quantidade', 'medidas', 'instalacao'
    ]
    
    dados_incompletos = {
        'nome_cliente': 'João',
        'contato': '(11) 99999-9999',
        # CEP faltando
        'endereco': 'Rua B',
        'numero': '456',
        # Resto faltando
    }
    
    campos_faltando = []
    for campo in campos_obrigatorios:
        if campo not in dados_incompletos or not dados_incompletos.get(campo):
            campos_faltando.append(campo)
    
    print(f"✓ Campos validados")
    print(f"✓ Campos obrigatórios: {len(campos_obrigatorios)}")
    print(f"✗ Campos preenchidos: {len(dados_incompletos)}")
    print(f"✗ Campos faltando ({len(campos_faltando)}): {', '.join(campos_faltando)}")
    
    return len(campos_faltando) > 0


def main():
    """Executa todos os testes"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "TESTES - SISTEMA DE ORÇAMENTO VIVACRM" + " " * 11 + "║")
    print("╚" + "=" * 58 + "╝")
    
    testes = [
        ("Teste Básico", teste_basico),
        ("Teste com Espaços", teste_com_espacos),
        ("Teste Dados Mínimos", teste_dados_minimos),
        ("Teste Múltiplas Medidas", teste_multiplas_medidas),
        ("Teste Validação", teste_validacao),
    ]
    
    resultados = []
    for nome, funcao_teste in testes:
        try:
            resultado = funcao_teste()
            resultados.append((nome, "✓ PASSOU"))
        except Exception as e:
            resultados.append((nome, f"✗ FALHOU: {str(e)}"))
    
    # Resumo
    print("\n" + "=" * 60)
    print("RESUMO DOS TESTES")
    print("=" * 60)
    for nome, resultado in resultados:
        print(f"{nome:<40} {resultado}")
    
    print("\n" + "=" * 60)
    passados = sum(1 for _, r in resultados if "PASSOU" in r)
    print(f"Total: {passados}/{len(resultados)} testes passaram")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
