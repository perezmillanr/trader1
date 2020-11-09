import pickle

class Dashboard:
	def __init__(self,name="Default Dashboard"):
		self.name=name
		self.path="dashboard.json"
		self.especies=[]
		
		savedDashboard=self.__loadDhasboard()
		if savedDashboard:
			self.especies=savedDashboard.especies

	def __repr__(self):
		"""Aca vamos a printear el Dashboard """
		return str(self.especies)

	def addEspecie(self,especie):
		"""Añaadir una especie al Dashbaord"""
		if especie not in self.especies:
			self.especies.append(especie.upper())
		self.__saveDashboard()
	def removeEspecie(self,especie):
		"""Remover una especie al Dashbaord"""
		if especie in self.especies:
			self.especies.remove(especie)
	def addExpression(self):
		"""Añadir una expresion al Dashbaord"""
		pass
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

#if __name__ == "__main__":
#	a=Dashboard()
#	a.addEspecie("YPFDs")
#	print(a)
