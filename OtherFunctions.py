import sys


def GetCredentialsCLI():
	"""Obtiene las credentiales de linea de comandos"""
	credentials={}
	if len(sys.argv)>=5:
		for arg in sys.argv:
			if arg=="-u":
				credentials["user"]=sys.argv[sys.argv.index(arg)+1]
			if arg=="-p":
				credentials["pwd"]=sys.argv[sys.argv.index(arg)+1]
	return credentials if "user" in credentials and "pwd" in credentials else False
			
