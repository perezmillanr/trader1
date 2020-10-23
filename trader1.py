#Autor ElRodrix
#2020
#Invertironline v2 API

import requests
import json
import sys
import AuthenticationToken
from IOL_Operations import *
from OtherFunctions import *

#### Aca arranca
if __name__ == "__main__":

	#Tenes que autorizar el API para usar el user y la pass
	token_ok = False
	#Chequeo si tengo credentiales en la CLI
	if GetCredentialsCLI():
		username=GetCredentialsCLI()["user"]
		password=GetCredentialsCLI()["pwd"]
		try:
			#Genero token
			token=AuthenticationToken.AuthenticationToken(username,password)
			token_ok = True
		except KeyError:
			print('Error de token. Reingrese los datos')
	#Sino tengo token con la CLI o no hay argumentos en la CLI, pido por standard input
	while not token_ok:
		username = input('Usuario: ')
		password = input('Contraseña: ')
		try:
			#Genero token
			token=AuthenticationToken.AuthenticationToken(username,password)
			token_ok = True
		except KeyError:
			print('Error de token. Reingrese los datos')

	#Levanto la cotizacion

	accion = input('Ingrese el pelpa (n para salir): ')

	while accion != 'n':	
		x=getCotizacion(token,accion,"t0")
		Cotizacion=x.text	
		print(x)
		print(Cotizacion)
		accion = input('Ingrese el pelpa (n para salir): ')