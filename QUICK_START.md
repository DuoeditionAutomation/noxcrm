# ⚡ Quick Start - 5 Minutos para Começar

## 🚀 Comece Agora!

### 1️⃣ Clone ou Extraia o Projeto

```bash
cd c:\Users\I9Dig\Documents\Projetos\VivaCRM
```

### 2️⃣ Execute o Script de Inicialização

**Windows:**
```bash
run.bat
```

**macOS/Linux:**
```bash
chmod +x run.sh
./run.sh
```

✅ O sistema criará automaticamente:
- Ambiente virtual
- Instalará dependências
- Criará arquivo `.env`

### 3️⃣ Acesse a Aplicação

Abra seu navegador e vá para:

```
http://localhost:5000
```

✅ Pronto! Sistema rodando! 🎉

---

## 📱 Testando Sem WhatsApp (Modo Simulação)

Já vem configurado! O sistema mostra uma mensagem de teste se não tiver credenciais do Twilio.

### Para Ver a Mensagem Formatada

```bash
python test_mensagens.py
```

---

## 🔧 Configurar WhatsApp (Opcional)

Quer enviar para WhatsApp de verdade? Siga 3 passos:

### Passo 1: Criar Conta Twilio

- Vá para [twilio.com](https://www.twilio.com)
- Clique em **Sign Up**
- Siga o guia de verificação

### Passo 2: Obter Credenciais

1. No [Twilio Console](https://www.twilio.com/console)
2. Copie seu:
   - `Account SID`
   - `Auth Token`
3. Configure WhatsApp Sandbox

### Passo 3: Atualizar .env

```bash
# Abra o arquivo .env (foi criado automaticamente)
# Preencha com suas credenciais:

TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=seu_token_aqui
TWILIO_PHONE_NUMBER=+55 11 98765-4321
WHATSAPP_GROUP_ID=+55 11 98765-4321
```

### Passo 4: Reiniciar

```bash
# Pressione Ctrl+C para parar
# Execute run.bat novamente
```

✅ Pronto! Agora envia para WhatsApp! 📱

---

## 📖 Documentação Completa

Depois de configurar o básico, leia:

1. **[README.md](README.md)** - Visão geral completa
2. **[TWILIO_SETUP.md](TWILIO_SETUP.md)** - Configuração WhatsApp detalhada
3. **[CUSTOMIZATION.md](CUSTOMIZATION.md)** - Personalizar cores, logo, campos
4. **[DEPLOYMENT.md](DEPLOYMENT.md)** - Colocar em servidor de verdade

---

## 🎯 Próximos Passos

### ✅ Básico
- [x] Sistema rodando localmente
- [ ] Testar com dados fictícios
- [ ] Customizar logo

### 🔧 Intermediário
- [ ] Configurar WhatsApp
- [ ] Mudar cores da marca
- [ ] Alterar tipos de trabalho/materiais

### 🚀 Avançado
- [ ] Deploy em servidor
- [ ] Adicionar banco de dados
- [ ] Implementar histórico

---

## 🆘 Problemas Comuns

### "Python não encontrado"
```bash
# Verifique a instalação
python --version

# Se não funcionar, reinstale Python
# Baixe em: python.org
```

### "Port 5000 já está em uso"
```bash
# Use outra porta no app.py:
# app.run(debug=True, port=5001)
```

### "Módulo não encontrado"
```bash
# Reinstale as dependências
pip install -r requirements.txt
```

### "CEP não funciona"
- É normal! O API pode estar indisponível às vezes
- O sistema funciona normalmente sem isso

---

## 🎨 Customizações Rápidas

### Mudar Cor Principal
Edite `static/css/style.css` (linha ~10):
```css
--primary-color: #FF6B35;  /* Mude para: #0066cc, #2ecc71, etc */
```

### Mudar Logo
Edite `templates/index.html` (linha ~14):
```html
<!-- Coloque seu logo em assets/ e atualize o caminho aqui -->
```

### Adicionar Campo
Edite `templates/index.html` e copie/cole um grupo de formulário

---

## 📋 Estrutura de Arquivos

```
VivaCRM/
├── app.py                    ← Lógica do servidor
├── requirements.txt          ← Dependências
├── .env                      ← Configurações (criar)
│
├── templates/
│   └── index.html           ← Interface
│
├── static/
│   ├── css/style.css        ← Estilos e cores
│   └── js/script.js         ← Lógica do formulário
│
├── assets/
│   └── logo.svg             ← Seu logo aqui
│
└── Documentação/
    ├── README.md
    ├── TWILIO_SETUP.md
    ├── CUSTOMIZATION.md
    └── DEPLOYMENT.md
```

---

## 💡 Dicas

1. **Teste Primeiro**: Preencha o formulário com dados fictícios
2. **Veja o Console**: Pressione F12 no navegador para debug
3. **Logs**: O servidor mostra tudo que acontece no terminal
4. **Salvar Progresso**: Git commit regular é uma boa ideia

---

## 🎯 Funcionalidades

✅ Formulário Multi-fase
✅ Validação em Tempo Real
✅ Design Moderno e Responsivo
✅ Integração WhatsApp (Twilio)
✅ Busca de CEP (ViaCEP)
✅ Múltiplas Medições
✅ Seleção Múltipla de Materiais
✅ 100% Customizável

---

## 📞 Precisa de Ajuda?

1. **Erro no Terminal?** - Veja a mensagem de erro
2. **WhatsApp?** - Leia [TWILIO_SETUP.md](TWILIO_SETUP.md)
3. **Aparência?** - Leia [CUSTOMIZATION.md](CUSTOMIZATION.md)
4. **Deploy?** - Leia [DEPLOYMENT.md](DEPLOYMENT.md)

---

## 🎉 Você Está Pronto!

O sistema está 100% funcional e pronto para usar. Divirta-se! 🚀

**Dúvidas?** Consulte a documentação ou teste com dados fictícios.

---

**Happy Coding!** 💻✨
