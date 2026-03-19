#!/bin/bash

# Script para iniciar o Sistema de Orçamento VivaCRM

echo "======================================"
echo "Sistema de Orçamento VivaCRM"
echo "======================================"
echo ""

# Verificar se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv venv
    echo ""
fi

# Ativar ambiente virtual
echo "Ativando ambiente virtual..."
source venv/bin/activate
echo ""

# Instalar dependências
echo "Instalando/atualizando dependências..."
pip install -q -r requirements.txt
echo ""

# Verificar se .env existe
if [ ! -f ".env" ]; then
    echo ""
    echo "ATENÇÃO: Arquivo .env não encontrado!"
    echo "Copie .env.example para .env e configure suas credenciais Twilio."
    echo ""
    cp .env.example .env
    echo "Arquivo .env criado. Configure-o antes de executar novamente!"
    exit 1
fi

# Executar aplicação
echo "======================================"
echo "Iniciando aplicação..."
echo "======================================"
echo ""
echo "Acesse: http://localhost:5000"
echo ""
echo "Pressione Ctrl+C para parar o servidor"
echo ""

python app.py
