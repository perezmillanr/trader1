import pickle
import requests
from IOL_Operations import *

class Dashboard:
	def __init__(self,name="Default Dashboard"):
		self.name=name
		self.path="dashboard.json"
		self.especies=[]
		self.expresiones=[]
		
		savedDashboard=self.__loadDhasboard()
		if savedDashboard:
			self.especies=savedDashboard.especies
			self.expresiones=savedDashboard.expresiones

	def __call__(self,token):
		"""Dashea"""
		print("Dashboard")
		print("--------------------------------------")
		for i in self.especies:
			p=getCotizacion(token,i[0],i[1],style="ultimoprecio")
			print(f"Especie: {i[0]}\nTiempo: {i[1]}\nPrecio: {p}")
			print("--------------------------------------")
		#expresiones
		for e in self.expresiones:
			print("Expresión: ",e)
			for a in sorted(e.split(sep="/"), key=len,reverse=True):
				for b in sorted(a.split(sep="*"), key=len,reverse=True):
					if not b.isdigit():
						e=e.replace(b,str(getCotizacion(token,b,"t0",style="ultimoprecio")))
			print("Valor:",eval(e))
			print("--------------------------------------")


	def __repr__(self):
		"""Aca vamos a printear el Dashboard """
		return str(self.especies)

	def addEspecie(self,especie):
		"""Añaadir una especie al Dashbaord"""
		if especie not in self.especies:
			self.especies.append([especie[0].upper(),especie[1]])
			self.__saveDashboard()
			print(f"{especie[0].upper()} añadida al Dashboard")
	def removeEspecie(self,especie):
		"""Remover una especie al Dashbaord"""
		for e in self.especies:
			if e[0]==especie:
				self.especies.remove(e)	
				self.__saveDashboard()
				print(f"{especie} removido del dashboard")	
	def addExpression(self,expresion):
		"""Añadir una expresion al Dashbaord"""
		if expresion:
			self.expresiones.append(expresion)
			self.__saveDashboard()
			print(f"Expresión añadida al Dashboard")
	def removeExpression(self,num):
		"""Remover una especie al Dashbaord"""
		self.expresiones.pop(int(num))

	def showdash(self):
		for i,exp in enumerate(self.expresiones):
			print(f"ID: {i}. Expresión: {exp}")

	def __saveDashboard(self):
		"""Guarda el Dashbaord en el file"""
		try:
			with open(self.path, 'wb') as f:
				pickle.dump(self,f)
		except Exception as e:
			print(f"No se pudo abrir el archivo: {e}")
	def __loadDhasboard(self):
		"""Levanta el Dashboard en el file"""
		try:
			with open(self.path, 'rb') as f:
				return pickle.load(f)
		except FileNotFoundError:
			return False				

