# 📱 Guia de Configuração Twilio + WhatsApp

## Passo 1: Criar Conta Twilio

1. Acesse [twilio.com](https://www.twilio.com)
2. Clique em **Sign Up**
3. Preencha seus dados e crie a conta
4. Verifique seu email

## Passo 2: Obter Credenciais

1. Acesse o [Twilio Console](https://www.twilio.com/console)
2. Você verá na página inicial:
   - **Account SID**: Copie e guarde
   - **Auth Token**: Copie e guarde (não compartilhe!)

## Passo 3: Configurar WhatsApp Sandbox

### Opção A: Usar WhatsApp Sandbox (Gratuito - para testes)

1. No console Twilio, vá para **Messaging > Services**
2. Clique em **Create Messaging Service**
3. Nomeie como "VivaCRM"
4. Selecione **WhatsApp** como canal
5. Vá para **Settings > Sandbox**
6. Escaneie o código QR com seu WhatsApp
7. Envie a mensagem sugerida
8. Você receberá um número Twilio

### Opção B: WhatsApp Business Account (Produção)

1. Entre em contato com o suporte Twilio
2. Eles ajudarão a vincular sua conta do WhatsApp Business
3. Você receberá um número verificado

## Passo 4: Configurar .env

1. Copie o arquivo `.env.example` para `.env`:
   ```bash
   copy .env.example .env
   ```

2. Abra `.env` e preencha:

   ```env
   TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   TWILIO_AUTH_TOKEN=your_auth_token_here
   TWILIO_PHONE_NUMBER=+55 11 98765-4321
   WHATSAPP_GROUP_ID=+55 11 98765-4321
   ```

## Passo 5: Encontrar ID de Grupo WhatsApp

Para enviar para um grupo WhatsApp:

### Método 1: Usar um Número Pessoal
- Use o número de WhatsApp pessoal do cliente
- Exemplo: `+55 11 98765-4321`

### Método 2: Usar Grupo WhatsApp
1. Crie um grupo no WhatsApp
2. Convide o número Twilio para o grupo
3. Copie o ID do grupo (formato similar a um número)
4. Use como `WHATSAPP_GROUP_ID`

⚠️ **NOTA**: Grupos têm limitações no Twilio Sandbox. Para produção, contate o suporte Twilio.

## Passo 6: Testar Conexão

### Teste 1: Verificar Credenciais
```python
from twilio.rest import Client

account_sid = "seu_account_sid"
auth_token = "seu_auth_token"

client = Client(account_sid, auth_token)
print("Credenciais válidas!")
```

### Teste 2: Enviar Mensagem de Teste
```python
from twilio.rest import Client

account_sid = "seu_account_sid"
auth_token = "seu_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Teste do Sistema de Orçamento VivaCRM",
    from_="whatsapp:+55_11_SEU_NUMERO",  # Seu número Twilio
    to="whatsapp:+55_11_NUMERO_DESTINO"    # Número do destinatário
)

print(f"Mensagem enviada: {message.sid}")
```

## 📊 Estrutura de Preços (Sandbox)

- **WhatsApp Sandbox**: Gratuito (com restrições)
- **Produção**: ~R$ 0,50 - R$ 2,00 por mensagem
- Consulte [pricing Twilio](https://www.twilio.com/whatsapp/pricing) para valores atualizados

## 🚀 Próximos Passos

1. ✅ Credenciais configuradas
2. ✅ WhatsApp Sandbox ativo
3. ✅ Arquivo `.env` preenchido
4. ✅ Aplicação testada
5. → Execute `python app.py` ou `run.bat`

## ❓ Troubleshooting

### Erro: "Invalid Account SID"
- Verifique se o SID foi copiado corretamente
- Sem espaços extras no começo ou fim

### Erro: "Invalid Auth Token"  
- Regenere o token no console Twilio
- Pode levar alguns minutos para ativar

### Mensagem não é entregue
- Verifique se o número tem WhatsApp ativo
- Confirme que o sandbox está ativo
- Veja se o número de destino é válido

### Sandbox expirou
- Sandbox expira após 72 horas de inatividade
- Escaneie o código QR novamente para reativar

## 📚 Documentação Oficial

- [Twilio WhatsApp API Docs](https://www.twilio.com/docs/whatsapp)
- [Twilio Python SDK](https://www.twilio.com/docs/libraries/python)
- [Twilio Console](https://www.twilio.com/console)

## 💡 Dicas

1. **Guarde suas credenciais**: Nunca compartilhe seu `Auth Token`
2. **Teste primeiro**: Use o sandbox antes de passar para produção
3. **Monitore uso**: Acompanhe o uso na dashboard Twilio
4. **Webhook (opcional)**: Configure callbacks para status de mensagens

---

**Precisa de ajuda?** Entre em contato com o suporte Twilio ou consulte os documentos oficiais.
