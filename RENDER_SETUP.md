# 🚀 Deploy VivaCRM no Render

## ✅ Pré-requisitos

1. **Conta no GitHub** - https://github.com (gratuita)
2. **Conta no Render** - https://render.com (gratuita)
3. **Git instalado** - https://git-scm.com

---

## 📝 Passo 1: Preparar Repositório GitHub

### 1.1 Criar repositório no GitHub

1. Acesse https://github.com/new
2. Nome do repositório: `vivacrm`
3. Descrição: `Sistema de Orçamentos com Flask`
4. Escolha **Public** ou **Private**
5. Clique em **Create repository**

### 1.2 Fazer push do código

No seu computador, abra PowerShell na pasta do projeto:

```powershell
cd "C:\Users\I9Dig\Documents\Projetos\VivaCRM"

# Inicializar git (se não foi feito)
git init

# Adicionar todos os arquivos
git add .

# Fazer commit
git commit -m "Initial commit: VivaCRM system"

# Adicionar repositório remoto (substitua SEU_USUARIO)
git remote add origin https://github.com/SEU_USUARIO/vivacrm.git

# Push para GitHub
git branch -M main
git push -u origin main
```

---

## 🔧 Passo 2: Configurar Render

### 2.1 Criar Web Service no Render

1. Acesse https://render.com
2. Faça login (ou crie conta)
3. Clique em **New +** → **Web Service**
4. Clique em **Connect a repository**
5. Selecione seu repositório `vivacrm`

### 2.2 Configurar Deploy

**Na página de criação do Web Service, preencha:**

| Campo | Valor |
|-------|-------|
| Name | `vivacrm` |
| Environment | `Python 3` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |
| Plan | `Free` |

### 2.3 Variáveis de Ambiente

1. Clique em **Environment**
2. Adicione (opcional):
   - `WHATSAPP_PHONE`: `+5519997328677`
   - `FLASK_ENV`: `production`

### 2.4 Deploy

Clique em **Create Web Service** e aguarde (~2-3 minutos)

Seu site estará em: **`https://vivacrm.onrender.com`**

---

## ✅ Verificar Deploy

1. Acesse: https://vivacrm.onrender.com
2. Veja o **Formulário** funcionando
3. Acesse o **Admin**: https://vivacrm.onrender.com/admin
4. Teste criando um tipo de trabalho

---

## 🔄 Fazer Updates

Sempre que fizer mudanças:

```powershell
cd "C:\Users\I9Dig\Documents\Projetos\VivaCRM"

git add .
git commit -m "Descrição da mudança"
git push origin main
```

**Render fará deploy automaticamente!** ✅

---

## ⚠️ Notas Importantes

### Banco de Dados
- SQLite funciona no Render (arquivo `orcamento.db`)
- **Dados NÃO persistem** se o dyno reinicar (free tier)
- Para dados persistentes, use PostgreSQL (upgrade necessário)

### WhatsApp
- `webbrowser.open()` **NÃO funciona** em produção (servidor)
- Você pode:
  - ✅ Testar localmente (`localhost:5000`)
  - ✅ Usar em servidor dedicado
  - 🔄 Considerar Evolution API ou Twilio para produção

### Tier Gratuito Render
- ✅ Inativo pode desligar (reinicia no acesso)
- ✅ 750 horas/mês
- ✅ SQLite incluído
- ❌ Sem HTTPS customizado

---

## 🆘 Troubleshooting

### Deploy falha - "ModuleNotFoundError"
```
Solução: Verifique requirements.txt e rode:
pip freeze > requirements.txt
git push origin main
```

### Banco de dados desaparece
```
Solução: Render pode resetar storage
Use PostgreSQL para dados persistentes
```

### Site está lento
```
Solução: Free tier pode desligar
Atualize para paid tier para melhor performance
```

---

## 🎯 Próximos Passos

1. ✅ Deploy no Render
2. ⚡ Testar sistema completo
3. 📊 Monitorar logs em tempo real
4. 🔐 Considerar autenticação para `/admin`
5. 💾 Backup do banco de dados

---

**Pronto para deploy!** 🚀

Qualquer dúvida, consulte:
- Docs Render: https://render.com/docs
- Docs GitHub: https://docs.github.com
- Docs Flask: https://flask.palletsprojects.com
