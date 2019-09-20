#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import socket
import sys
 
# Creando un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Conecta el socket en el puerto cuando el servidor esté escuchando
server_address = ('localhost', 10000)
print (sys.stderr, 'Conectando a %s puerto %s' % server_address)
sock.connect(server_address)
inicio = input("Ingresa el comando para iniciar: ")
if(inicio=="telnet" or inicio=="Telnet" or inicio=="TELNET"):
	ejecutar=True
	while ejecutar:
		comando= input("")
		if(comando!="exit"):
			try:
				# Enviando datos
				print (comando)
				sock.sendall(comando.encode())
					 
				# Buscando respuesta
				amount_received = 0
				amount_expected = len(message)
					     
				while amount_received < amount_expected:
					data = sock.recv(19)
					amount_received += len(data)
					print (sys.stderr, 'recibiendo "%s"' % data)
					 
			except:
				print (sys.stderr, 'cerrando socket')
				sock.close()
					
		else:
			sock.close()
			ejecutar=False
else:
	print("Ingresa un comando valido")