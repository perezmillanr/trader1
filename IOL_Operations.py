import requests
import json
import datetime
#def getInstrumento_FIXME():

#	mercado="BYMA"
#	especie="PAMP"
#	plazo='t0'

#	baseurl="https://api.invertironline.com"
#	endpoint=baseurl+"/api/v2/argentina/Titulos/Cotizacion/Instrumentos"
	#endpoint=baseurl+"/api/v2/estadocuenta" #Estado de mi cuenta
#	header={"Accept":"application/json",
#	        'Authorization':"Bearer "+token.getBearerToken()
#	        }

#	param={ 'api_key':token.getBearerToken()}

#	print(header)
#	print(param)
#	print(endpoint)

#	x=requests.get(endpoint,data=param,headers=header)


def getCotizacion(token,especie,plazo,style="raw"):
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

	#Dependiendo del estido damos consas diferentes
	if style=="raw":
		return requests.get(endpoint,data=param,headers=header)
	if style=="ultimoprecio":
		return json.loads(requests.get(endpoint,data=param,headers=header).text)["ultimoPrecio"]
	else:
		return requests.get(endpoint,data=param,headers=header)

def getEstadoCuenta(token):
	"""Devuelve el estado de la cuenta"""
	baseurl="https://api.invertironline.com"
	endpoint=baseurl+"/api/v2/estadocuenta"
	header={"Accept":"application/json",
	        'Authorization':"Bearer "+token.getBearerToken()
	        }

	param={'api_key':token.getBearerToken()}

	return requests.get(endpoint,data=param,headers=header)

#def getOperacion_FIXME(token,id):
#	baseurl="https://api.invertironline.com"
#	endpoint=baseurl+"/api/v2/operacion/"+str(id)
#	header={"Accept":"application/json",
#	        'Authorization':"Bearer "+token.getBearerToken()
#	        }
#	param={'api_key':token.getBearerToken()}
#	return requests.get(endpoint,data=param,headers=header)


def delOperacion(token,id):
	"""Borra una operación"""
	baseurl="https://api.invertironline.com"
	endpoint=baseurl+"/api/v2/operaciones/"+str(id)
	header={"Accept":"application/json",
	        'Authorization':"Bearer "+token.getBearerToken()
	        }
	param={'api_key':token.getBearerToken()}

	print(endpoint)
	print(header)
	return requests.delete(endpoint,data=param,headers=header)


def getOperaciones(token):
	"""Devuelve las operaciones"""
	baseurl="https://api.invertironline.com"
	endpoint=baseurl+"/api/v2/operaciones"
	header={"Accept":"application/json",
	        'Authorization':"Bearer "+token.getBearerToken()
	        }
	param={'api_key':token.getBearerToken()}
	return requests.get(endpoint,data=param,headers=header)


def comprar(token,especie,plazo,precio,cantidad,validez=24):
	"""Pone una orden de compra"""

	d=datetime.datetime.now()+datetime.timedelta(days=validez)

	baseurl="https://api.invertironline.com"
	endpoint=baseurl+"/api/v2/operar/Comprar"
	header={"Accept":"application/json",
	        'Authorization':"Bearer "+token.getBearerToken()
	        }

	param={ 'simbolo':especie,
			'mercado':'bCBA',
			'plazo':plazo,
			'cantidad':cantidad,
			'precio':precio,
			'validez': d.isoformat('T',"milliseconds")+"Z",
			'api_key':token.getBearerToken()}
	return requests.post(endpoint,data=param,headers=header)
