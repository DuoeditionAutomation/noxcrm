@echo off
REM Script para iniciar o Sistema de Orçamento VivaCRM

echo ======================================
echo Sistema de Orçamento VivaCRM
echo ======================================
echo.

REM Verificar se o ambiente virtual existe
if not exist "venv" (
    echo Criando ambiente virtual...
    python -m venv venv
    echo.
)

REM Ativar ambiente virtual
echo Ativando ambiente virtual...
call venv\Scripts\activate.bat
echo.

REM Instalar dependências
echo Instalando/atualizando dependências...
pip install -q -r requirements.txt
echo.

REM Verificar se .env existe
if not exist ".env" (
    echo.
    echo ATENÇÃO: Arquivo .env não encontrado!
    echo Copie .env.example para .env e configure suas credenciais Twilio.
    echo.
    copy .env.example .env
    echo Arquivo .env criado. Configure-o antes de executar novamente!
    pause
    exit /b
)

REM Executar aplicação
echo ======================================
echo Iniciando aplicação...
echo ======================================
echo.
echo Acesse: http://localhost:5000
echo.
echo Pressione Ctrl+C para parar o servidor
echo.

python app.py

pause
