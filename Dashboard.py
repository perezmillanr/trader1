import json

class Dashboard:
	def __init__(self,name="Default Dashboard"):
		self.name=name
		self.path="/dashboard.json"
		pass
	def __repr__(self):
		"""Aca vamos a printear el Dashboard """
		pass
	def addEspecie(self):
		"""Añaadir una especie al Dashbaord"""
		pass
	def removeEspecie(self):
		"""Remover una especie al Dashbaord"""
		pass
	def addExpression(self):
		"""Añadir una expresion al Dashbaord"""
		pass
	def __saveDashboard(self):
		"""Guarda el Dashbaord en el file"""
		pass
	def __loadDhasboard(self):
		"""Levanta el Dashboard en el file"""
		pass

	pass
