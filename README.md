# Servidor de eco con sockets y threading

**Alumno:** Gian Oliva  
**Materia:** Programación sobre Redes

El servidor atiende a varios clientes al mismo tiempo. Devuelve cada mensaje al cliente que lo envió.

## Uso

Necesitás Python 3.9 o posterior. No hay dependencias externas.

En una terminal, ejecutá `python servidor.py`. En otra, ejecutá `python cliente.py`. Podés abrir más terminales con `cliente.py` para probar varias conexiones.

- `/users` muestra los clientes conectados, identificados por IP y puerto.
- `/adios` cierra solamente la conexión de ese cliente.

Por defecto ambos programas usan `127.0.0.1:12345`, así que funcionan en la misma computadora. Para probar entre dos computadoras de una red local, cambiá `HOST` en el servidor a `0.0.0.0` y `HOST` en el cliente a la IP local del servidor. El puerto debe coincidir.
