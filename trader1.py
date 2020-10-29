#Autor ElRodrix
#2020
#Invertironline v2 API

import requests
import json
import sys
import AuthenticationToken as AuthTK
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
			token=AuthTK.AuthenticationToken(token_dict = AuthTK.requestToken(username,password))
			token_ok = True
		except KeyError:
			print('Error de token. Reingrese los datos')
	#Sino tengo token con la CLI o no hay argumentos en la CLI, pido por standard input
	while not token_ok:
		username = input('Usuario: ')
		password = input('Contraseña: ')
		try:
			#Genero token
			token=AuthTK.AuthenticationToken(token_dict = AuthTK.requestToken(username,password))
			token_ok = True
		except KeyError:
			print('Error de token. Reingrese los datos')


	while True:
		accion = input('Ingrese Comando ("help" para ver los comandos): ')			

		if accion.lower()=="cot":
			especie = input('Ingrese el especie (n para salir): ')
			if especie == 'n':	
				continue
			else:
				t_ = input('Ingrese el tiempo (t0,t1,t2): ')
				print(getCotizacion(token,accion,t_))
				print(getCotizacion(token,accion,t_).text)
				continue
		if accion.lower()=="help":
			print("Comandos:")
			print("cot - Obtener Cotizacion de una Especie")
			print("salir - Salir de la aplicación")
			print("help - Obtener Lista de Comandos")
		if accion.lower()=="salir":
			break
		print ("Comando no reconocido")



	#Levanto la cotizacion

#	accion = input('Ingrese el pelpa (n para salir): ')
#	while accion != 'n':	
#		x=getCotizacion(token,accion,"t0")
#		Cotizacion=x.text	
#		print(x)
#		print(Cotizacion)
#		accion = input('Ingrese el pelpa (n para salir): ')