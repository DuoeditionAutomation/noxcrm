# 🚀 Guia de Deployment - Sistema de Orçamento VivaCRM

Este documento contém instruções para colocar o sistema em produção.

## 📋 Pré-requisitos

- Python 3.8+
- Servidor (VPS, Heroku, PythonAnywhere, etc.)
- Domínio (opcional)
- Certificado SSL (obrigatório para HTTPS)

## 🏠 Opção 1: Deployment Local (Windows/Mac/Linux)

### 1.1 Usando WSGI Server (Gunicorn)

```bash
# Instalar gunicorn
pip install gunicorn

# Executar com Gunicorn (produção)
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app
```

### 1.2 Usar Supervisor (Para manter rodando)

```bash
# Instalar supervisor
pip install supervisor

# Criar arquivo de configuração
sudo nano /etc/supervisor/conf.d/vivacrm.conf
```

Adicione:
```ini
[program:vivacrm]
command=/path/to/venv/bin/gunicorn --workers 4 app:app
directory=/path/to/project
autostart=true
autorestart=true
stderr_logfile=/var/log/vivacrm.err.log
stdout_logfile=/var/log/vivacrm.out.log
```

```bash
# Recarregar supervisor
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start vivacrm
```

## ☁️ Opção 2: Heroku

### 2.1 Instalar Heroku CLI

```bash
# Windows
choco install heroku-cli

# macOS
brew tap heroku/brew && brew install heroku

# Linux
curl https://cli-assets.heroku.com/install.sh | sh
```

### 2.2 Criar Procfile

```bash
echo "web: gunicorn app:app" > Procfile
pip install gunicorn
```

### 2.3 Deploy

```bash
# Fazer login
heroku login

# Criar app
heroku create seu-app-vivacrm

# Adicionar variáveis de ambiente
heroku config:set TWILIO_ACCOUNT_SID=seu_sid
heroku config:set TWILIO_AUTH_TOKEN=seu_token
heroku config:set TWILIO_PHONE_NUMBER=seu_numero
heroku config:set WHATSAPP_GROUP_ID=seu_grupo

# Deploy
git push heroku main

# Ver logs
heroku logs --tail
```

## 🐳 Opção 3: Docker

### 3.1 Criar Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

### 3.2 Criar docker-compose.yml

```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      FLASK_ENV: production
      TWILIO_ACCOUNT_SID: ${TWILIO_ACCOUNT_SID}
      TWILIO_AUTH_TOKEN: ${TWILIO_AUTH_TOKEN}
      TWILIO_PHONE_NUMBER: ${TWILIO_PHONE_NUMBER}
      WHATSAPP_GROUP_ID: ${WHATSAPP_GROUP_ID}
    volumes:
      - .:/app
```

### 3.3 Executar

```bash
docker-compose up -d
```

## 🔒 Configurações de Produção

### 4.1 Atualizar app.py para Produção

```python
# No final do app.py, altere:
if __name__ == '__main__':
    # Desenvolvimento
    # app.run(debug=True, port=5000)
    
    # Produção
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### 4.2 Variáveis de Ambiente Importantes

```bash
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=gere-uma-chave-segura-aqui
TWILIO_ACCOUNT_SID=seu_sid
TWILIO_AUTH_TOKEN=seu_token
TWILIO_PHONE_NUMBER=seu_numero
WHATSAPP_GROUP_ID=seu_grupo
```

Gerar SECRET_KEY:
```python
import secrets
print(secrets.token_hex(32))
```

## 🔐 SSL/HTTPS

### 5.1 Usando Let's Encrypt (Grátis)

```bash
# Instalar Certbot
sudo apt-get install certbot python3-certbot-nginx

# Gerar certificado
sudo certbot certonly --standalone -d seu-dominio.com

# Renovação automática
sudo certbot renew --dry-run
```

### 5.2 Configurar Nginx com SSL

```nginx
server {
    listen 443 ssl;
    server_name seu-dominio.com;

    ssl_certificate /etc/letsencrypt/live/seu-dominio.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/seu-dominio.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

# Redirecionar HTTP para HTTPS
server {
    listen 80;
    server_name seu-dominio.com;
    return 301 https://$server_name$request_uri;
}
```

Recarregar Nginx:
```bash
sudo systemctl restart nginx
```

## 📊 Monitoramento

### 6.1 Logs

```bash
# Ver logs em tempo real
tail -f /var/log/vivacrm.out.log

# Ver erros
tail -f /var/log/vivacrm.err.log
```

### 6.2 Uptime Monitoring

1. Usar serviços como:
   - UptimeRobot (uptime.com)
   - Pingdom
   - StatusCake

2. Configurar alertas para quando o site cair

### 6.3 Performance

- Usar ferramentas como:
  - NewRelic
  - Datadog
  - Scout APM

## 🔄 Auto-Scaling (Opcional)

Se usar Heroku:
```bash
heroku ps:scale web=2
```

## 🗄️ Banco de Dados (Futuro)

Se precisar guardar orçamentos:

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/vivacrm'
db = SQLAlchemy(app)

class Orcamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_cliente = db.Column(db.String(100), nullable=False)
    # ... outros campos
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

# Criar tabelas
with app.app_context():
    db.create_all()
```

## 📝 Checklist de Deploy

- [ ] Variáveis de ambiente configuradas
- [ ] `debug=False` em produção
- [ ] SSL/HTTPS ativo
- [ ] Credenciais Twilio testadas
- [ ] Logs configurados
- [ ] Backup automático (se usar banco)
- [ ] Monitoramento ativo
- [ ] Email de notificação de erros
- [ ] Domínio apontando corretamente
- [ ] Firewall configurado

## 🆘 Troubleshooting

### "Connection refused"
- Verificar se a porta 5000 está aberta
- Checklist de firewall

### "Module not found"
```bash
pip install -r requirements.txt
```

### "Permission denied"
```bash
chmod +x run.sh
```

### Mensagens não enviadas
- Verificar credenciais Twilio
- Verificar logs: `heroku logs --tail`

## 📞 Suporte

- Documentação Flask: https://flask.palletsprojects.com/
- Gunicorn: https://gunicorn.org/
- Heroku: https://www.heroku.com/
- Twilio: https://www.twilio.com/docs

---

**Pronto para produção!** 🚀
