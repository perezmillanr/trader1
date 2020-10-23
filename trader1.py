#Autor ElRodrix
#2020
#Invertironline v2 API

import requests
import json
import AuthenticationToken
from IOL_Operations import *

#### Aca arranca
if __name__ == "__main__":
	
	#Genero token
	#Tenes que autorizar el API para usar el user y la pass
	token_ok = False
	while not token_ok:
		username = input('Usuario: ')
		password = input('Contraseña: ')
		try:
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