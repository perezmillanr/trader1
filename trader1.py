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
	#Levanto el Dashboard
	dash=Dashboard()
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
		comando=comando.lower()
		if comando=="cot":
			especie = input('Ingrese el especie (n para cancelar): ')
			if especie == 'n':	
				continue
			else:
				t_ = input('Ingrese plazo (t0,t1,t2): ')
				print(getCotizacion(token,especie,t_).text)
				continue

		if comando=="addexp":
			dash.addExpression(input ("Inserte Expresión: "))
			continue
		if comando=="remexp":
			dash.removeExpression(input ("Inserte Expresión a remover: "))
			continue			
		if comando=="dashexp":
			dash.showdash()
			continue
		if comando=="add":
			especie = input('Ingrese el especie para añadir (n para cancelar): ')
			if especie == 'n':	
				continue
			else:
				t_ = input('Ingrese plazo (t0,t1,t2): ')
				dash.addEspecie([especie,t_])
				print()
				continue
		if comando=="rem":
			especie = input('Ingrese el especie para remover (n para cancelar): ')
			if especie == 'n':	
				continue
			else:
				dash.removeEspecie(especie.upper())
				continue
		if comando=="dash":
			dash(token)
			continue
		if comando=="cotp":
			especie = input('Ingrese el especie (n para cancelar): ')
			if especie == 'n':	
				continue
			else:
				t_ = input('Ingrese plazo (t0,t1,t2): ')
				print(getCotizacion(token,especie,t_,style="ultimoprecio"))
				continue


		if comando=="del":
			operacion = input('Ingrese la orden (n para cancelar): ')
			if operacion == 'n':	
				continue
			else:
				print(delOperacion(token,operacion))
				continue

		if comando=="comprar":
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
		if comando=="estado":
				print(getEstadoCuenta(token).text)
				continue
		if comando.startswith("getop"):
			if comando=="getop":
				print(getOperaciones(token).text)
			else:
				id=int(comando.split()[-1])
				print(id)
			continue	
		if comando=="help":
			print("Comandos:")
			print("cot - Obtener Cotizacion de una Especie")
			print("cotp - Obtener ultimo precio de una Especie")
			print("comprar - Colocar orden de compra")
			print("del - Borrar una orden")
			print("estado - Obtener Estado de cuenta")
			print("salir - Salir de la aplicación")
			print("help - Obtener Lista de Comandos")
			print("\nComandos de Dashboard:")
			print("add - Añade especie al Dashboard")
			print("rem - Remueve especie al Dashboard")
			print("dash - Muestra el dashboard")
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
