import socket


HOST = "127.0.0.1"
PORT = 12345


def iniciar_cliente():
    try:
        with socket.create_connection((HOST, PORT)) as cliente:
            with cliente.makefile("r", encoding="utf-8") as entrada:
                print(entrada.readline(), end="")

                while True:
                    mensaje = input("> ")
                    cliente.sendall((mensaje + "\n").encode("utf-8"))
                    respuesta = entrada.readline()
                    if not respuesta:
                        print("El servidor cerró la conexión.")
                        break
                    print(respuesta, end="")
                    if mensaje.strip().lower() == "/adios":
                        break
    except ConnectionRefusedError:
        print("No se pudo conectar. Iniciá primero servidor.py.")
    except (KeyboardInterrupt, EOFError):
        print("\nCliente cerrado.")
    except OSError as error:
        print(f"Error de conexión: {error}")


if __name__ == "__main__":
    iniciar_cliente()
