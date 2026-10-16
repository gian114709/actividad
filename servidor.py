import socket
import threading


HOST = "127.0.0.1"
PORT = 12345
clientes = {}
lock = threading.Lock()


def enviar(conexion, mensaje):
    conexion.sendall((mensaje + "\n").encode("utf-8"))


def atender_cliente(conexion, direccion):
    nombre = f"{direccion[0]}:{direccion[1]}"
    try:
        with conexion:
            enviar(conexion, f"Conectado como {nombre}. Comandos: /users y /adios")
            with conexion.makefile("r", encoding="utf-8") as entrada:
                for linea in entrada:
                    mensaje = linea.removesuffix("\n")
                    comando = mensaje.strip().lower()

                    if comando == "/adios":
                        with lock:
                            clientes.pop(conexion, None)
                        enviar(conexion, "Hasta luego. Conexión finalizada.")
                        break

                    if comando == "/users":
                        with lock:
                            usuarios = sorted(clientes.values())
                        enviar(conexion, f"Usuarios conectados ({len(usuarios)}): " + ", ".join(usuarios))
                    else:
                        enviar(conexion, mensaje)
    except (OSError, UnicodeError):
        pass
    finally:
        with lock:
            clientes.pop(conexion, None)
        print(f"Cliente desconectado: {nombre}")


def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((HOST, PORT))
        servidor.listen()
        print(f"Servidor escuchando en {HOST}:{PORT}")

        try:
            while True:
                conexion, direccion = servidor.accept()
                nombre = f"{direccion[0]}:{direccion[1]}"
                with lock:
                    clientes[conexion] = nombre
                print(f"Cliente conectado: {nombre}")
                threading.Thread(target=atender_cliente, args=(conexion, direccion), daemon=True).start()
        except KeyboardInterrupt:
            print("\nServidor detenido.")


if __name__ == "__main__":
    iniciar_servidor()
