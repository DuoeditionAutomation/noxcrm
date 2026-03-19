#!/usr/bin/env python3
"""
Script de Inicialização com Detecção de IP
Mostra URL de acesso tanto local quanto na rede
"""

import socket
import sys
import os

def get_local_ip():
    """Obtém o IP local da máquina"""
    try:
        # Conecta a um servidor (sem enviar dados)
        # para descobrir qual IP está ativo
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def get_hostname():
    """Obtém o nome do computador"""
    return socket.gethostname()

def main():
    print("\n" + "="*70)
    print(" " * 15 + "🎯 SISTEMA DE ORÇAMENTO VIVACRM")
    print("="*70)
    
    local_ip = get_local_ip()
    hostname = get_hostname()
    port = 5000
    
    print("\n📍 IP Local: " + local_ip)
    print("🖥️  Computador: " + hostname)
    print("🔌 Porta: " + str(port))
    print("\n" + "="*70)
    
    print("\n✨ ACESSOS DISPONÍVEIS:\n")
    
    print("📱 LOCAL (Este Computador):")
    print(f"   Formulário: http://localhost:{port}")
    print(f"   Admin:      http://localhost:{port}/admin\n")
    
    print("🌐 REDE (Qualquer Dispositivo Conectado):")
    print(f"   Formulário: http://{local_ip}:{port}")
    print(f"   Admin:      http://{local_ip}:{port}/admin\n")
    
    print("="*70)
    print("\n💡 DICA: Compartilhe o IP acima para outros acessarem!\n")
    
    # Iniciar Flask
    print("🚀 Iniciando servidor...\n")
    
    os.system("python app.py")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Servidor encerrado pelo usuário.")
        sys.exit(0)
