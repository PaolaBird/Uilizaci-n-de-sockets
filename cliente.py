#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import socket
import sys
 
# Creando un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Conecta el socket en el puerto cuando el servidor esté escuchando
server_address = ('', 40518)
print >>sys.stderr, 'Conectando a %s puerto %s' % server_address
sock.connect(server_address)
comandos = ['ls','pwd','cd']
try:
     
    
# Enviando datos
    cmd =raw_input("")
    if cmd != 'exit':
        if cmd in comandos:
        	print >>sys.stderr, '%s' % cmd
        	sock.sendall(cmd)
 
        	# Buscando respuesta
        	amount_received = 0
        	amount_expected = len(cmd)
     
       		while amount_received < amount_expected:
        		data = sock.recv(100)
        		amount_received += len(data)
            	print >>sys.stderr, '%s' % data
         
        else:
          print >>sys.stderr, 'Comando no valido'
 
finally:
    print >>sys.stderr, 'Cerrando socket'
    sock.close()
