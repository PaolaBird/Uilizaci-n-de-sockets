#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import socket
import sys
import subprocess

# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Cierra los sockets abiertos que podria no permitir la ejecución de este servidor
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Enlace de socket y puerto
ip = raw_input("Ingresa la ip servidor ")
if(len(ip)>0):
	server_address = ('localhost', 40518)
else:
	server_address = ('%s' %ip, 40518)

print >>sys.stderr, 'Iniciando en el %s puerto %s' % server_address
sock.bind(server_address)

# Escuchando conexiones entrantes
sock.listen(1)
 
while True:
    # Esperando conexion
    print >>sys.stderr, 'Esperando para conectarse...'
    connection, client_address = sock.accept()
    subprocess.check_output('clear', shell=True)
    try:
        print >>sys.stderr, 'Conectado desde:', client_address
 
        # Recibe los datos en trozos y reetransmite
        while True:
            data = connection.recv(100)
            print >>sys.stderr, '%s' % data
            if data == 'cd':
                a= subprocess.check_output('pwd', shell=True)
                b= subprocess.check_output('cd', shell=True)
                c= subprocess.check_output('pwd', shell=True)
                result = """{}
							{}
							{}""".format(a,b,c)
                connection.sendall(result)
                break
            else:
                result= subprocess.check_output(data, shell=True)
                if result>0:
                    if data:
                        connection.sendall(result)
                    else:
                        print >>sys.stderr, 'Respuesta enviada', client_address
                        break
                else:
                    print >> sys.stderr, 'El comando %s no existe' %data
    finally:
        # Cerrando conexion
        connection.close()

