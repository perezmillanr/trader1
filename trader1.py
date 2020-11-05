#Autor ElRodrix
#2020
#Invertironline v2 API

import requests
import json
import sys
import AuthenticationToken as AuthTK
from IOL_Operations import *
from OtherFunctions import *
from Dashboard import *

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

	print("Bienvenido")
	print('Ingrese comando ("help" para ver los comandos):')
	while True:
		comando = input('>> ')			
		if comando.lower()=="cot":
			especie = input('Ingrese el especie (n para cancelar): ')
			if especie == 'n':	
				continue
			else:
				t_ = input('Ingrese plazo (t0,t1,t2): ')
				print(getCotizacion(token,especie,t_).text)
				continue
		if comando.lower()=="cotp":
			especie = input('Ingrese el especie (n para cancelar): ')
			if especie == 'n':	
				continue
			else:
				t_ = input('Ingrese plazo (t0,t1,t2): ')
				print(getCotizacion(token,especie,t_,style="ultimoprecio"))
				continue


		if comando.lower()=="del":
			operacion = input('Ingrese la orden (n para cancelar): ')
			if operacion == 'n':	
				continue
			else:
				print(delOperacion(token,operacion))
				continue

		if comando.lower()=="comprar":
			especie = input('Ingrese el especie (n para cancelar): ')
			if especie == 'n':	
				continue
			plazo = input('Ingrese plazo (t0,t1,t2) (n para cancelar):')
			if plazo == 'n':	
				continue
			precio = input('Ingrese el precio (n para cancelar): ')
			if precio == 'n':	
				continue
			cantidad = input('Ingrese cantidad (n para cancelar):')
			if cantidad == 'n':	
				continue

			print(comprar(token,especie,plazo,precio,cantidad).text)
			continue

		if comando.lower()=="estado":
				print(getEstadoCuenta(token).text)
				continue

		if comando.lower().startswith("getop"):
			if comando.lower()=="getop":
				print(getOperaciones(token).text)
			else:
				id=int(comando.split()[-1])
				print(id)
			continue	
		if comando.lower()=="help":
			print("Comandos:")
			print("cot - Obtener Cotizacion de una Especie")
			print("cotp - Obtener ultimo precio de una Especie")
			print("comprar - Colocar orden de compra")
			print("del - Borrar una orden")
			print("estado - Obtener Estado de cuenta")
			print("salir - Salir de la aplicación")
			print("help - Obtener Lista de Comandos")
			continue
		if comando.lower()=="salir":
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
