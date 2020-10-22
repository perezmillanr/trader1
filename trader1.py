#Autor ElRodrix
#2020
#Invertironline v2 API

import requests
import json

class AuthenticationToken:
	def __init__(self,username,password):
		endpoint= "https://api.invertironline.com/token"
		header={"Content-Type":"application/x-www-form-urlencoded"}
		param={'username':username,'password':password,"grant_type":"password"}

		HTTSrespose=requests.post(endpoint, data = param, headers = header)

		response=json.loads(HTTSrespose.text)

		self.bearerToken=response["access_token"]
		self.refreshToken=response["refresh_token"]
		self.expirationinseconds=response["expires_in"]
		self.issuedate=response[".issued"]
		self.expirationdate=response[".expires"]

	def getRefreshToken(self):
		pass
	def getBearerToken(self):
		return self.bearerToken
	def getRefreshToken(self):
		return self.refreshToken

def getInstrumento_FIXME():
	"""Es una verga, no trae nada copado"""

	mercado="BYMA"
	especie="PAMP"
	plazo='t0'

	baseurl="https://api.invertironline.com"
	endpoint=baseurl+"/api/v2/argentina/Titulos/Cotizacion/Instrumentos"
	#endpoint=baseurl+"/api/v2/estadocuenta" #Estado de mi cuenta
	header={"Accept":"application/json",
	        'Authorization':"Bearer "+token.getBearerToken()
	        }

	param={ 'api_key':token.getBearerToken()}

	print(header)
	print(param)
	print(endpoint)

	x=requests.get(endpoint,data=param,headers=header)


def getCotizacion(token,especie,plazo):
	"""Trae la cotizacion de una especia en BCBA"""
	baseurl="https://api.invertironline.com"
	endpoint=baseurl+"/api/v2/bCBA/Titulos/"+especie+"/Cotizacion"
	#endpoint=baseurl+"/api/v2/estadocuenta" #Estado de mi cuenta
	header={"Accept":"application/json",
	        'Authorization':"Bearer "+token.getBearerToken()
	        }

	param={ 'model.simbolo':especie,
			'model.mercado':'bCBA',
			'model.plazo':plazo,
			'api_key':token.getBearerToken()}
	return requests.get(endpoint,data=param,headers=header)


#### Aca arranca

#Genero token
#Tenes que autorizar el API para usar el user y la pass
token=AuthenticationToken("usuario","contrasena")

#Levanto la cotizacion
x=getCotizacion(token,"YPFD","t0")
Cotizacion=x.text

print(x)
print(Cotizacion)




