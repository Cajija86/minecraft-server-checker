import time
from mcstatus import JavaServer

# Cambia esto por la dirección de tu servidor de Aternos
server_address = "Cajija86.aternos.me"
server_port = 26291  # Puerto de tu servidor

while True:
    try:
        # Intenta conectarse al servidor
        server = JavaServer(server_address, server_port)
        status = server.status()
        
        print(f"Servidor está en línea: {status.players.online} jugadores conectados.")
        
        # Espera 30 segundos antes de volver a comprobar
        time.sleep(30)
        
    except Exception as e:
        print(f"Servidor no está disponible, error: {e}")
        time.sleep(30)
