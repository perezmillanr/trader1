import requests
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


