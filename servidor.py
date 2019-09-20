#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import socket
import sys
import subprocess
from subprocess import Popen
 
# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Cierra los sockets abiertos que podria no permitir la ejecución de este servidor
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Enlace de socket y puerto
server_address = ('localhost', 10000)
sock.bind(server_address)

# Escuchando conexiones entrantes
sock.listen(1)
 
while True:
    # Esperando conexion
    print (sys.stderr, 'Esperando para conectarse...')
    connection, client_address = sock.accept()

    try:
        print (subprocess.run("cls", shell=True), 'Conectado con: ', client_address)
 
        # Recibe los datos en trozos y reetransmite
        while True:
            data = connection.recv(19)
            print (data)
            #respuesta= subprocess.run(data.decode(), shell=True)
            p = Popen([data.decode()], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            output, errors = p.communicate()
            if data:
                print (sys.stderr, 'enviando mensaje de vuelta al cliente')
                connection.sendall(output.encode())
            else:
                print (sys.stderr, 'no hay mas datos', client_address)
                break
             
    finally:
        # Cerrando conexion
        connection.close()