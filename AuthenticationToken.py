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

		print(self.expirationdate)

	def getRefreshToken(self):
		pass
	def getBearerToken(self):
		return self.bearerToken
	def getRefreshToken(self):
		return self.refreshToken
