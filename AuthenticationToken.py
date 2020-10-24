import requests
import json
import pickle
from datetime import datetime

def requestToken(username, password):
    endpoint= 'https://api.invertironline.com/token'
    header={"Content-Type":"application/x-www-form-urlencoded"}
    param={'username':username,'password':password,"grant_type":"password"}
    HTTSrespose=requests.post(endpoint, data = param, headers = header)
    response=json.loads(HTTSrespose.text)
    return response
    
def refreshToken(refreshToken):
    endpoint= 'https://api.invertironline.com/token'
    header={"Content-Type":"application/x-www-form-urlencoded"}
    param={'refresh_token':refreshToken,'grant_type':'refresh_token'}
    HTTSrespose=requests.post(endpoint, data = param, headers = header)
    response=json.loads(HTTSrespose.text)
    return response

class AuthenticationToken:
    def __init__(self, token_file = '', token_dict = 0):
        self.bearerToken = ''
        if token_file:
            try:
                with open(token_file, 'rb') as token_f:
                    savedToken = pickle.load(token_f)
            except FileNotFoundError:
                    savedToken = False
    
            if savedToken:
                self.expDate = datetime.strptime(savedToken.expDate, '%a, %d %b %Y %X %Z')
                self.issDate = datetime.strptime(savedToken.issDate, '%a, %d %b %Y %X %Z')
                self.refExpDate = datetime.strptime(savedToken.refExpDate, '%a, %d %b %Y %X %Z')
                self.bearerToken = savedToken.bearerToken
                self.expInSec = savedToken.expInSec
                self.refreshToken = savedToken.refreshToken
                self.tokenType = savedToken.tokenType
        
        elif token_dict:
            self.expDate = datetime.strptime(token_dict['.expires'], '%a, %d %b %Y %X %Z')
            self.issDate = datetime.strptime(token_dict['.issued'], '%a, %d %b %Y %X %Z')
            self.refExpDate = datetime.strptime(token_dict['.refreshexpires'], '%a, %d %b %Y %X %Z')
            self.bearerToken = token_dict['access_token']
            self.expInSec = token_dict['expires_in']
            self.refreshToken = token_dict['refresh_token']
            self.tokenType = token_dict['token_type']
            with open('token_file', 'wb') as token_f:
                pickle.dump(self,token_f)

        

    def getBearerToken(self):
        if self.bearerToken:
            if self.expDate > datetime.utcnow():
                return self.bearerToken
            elif self.refExpDate > datetime.utcnow():
                tk_dict = refreshToken(self.refreshToken)
                return self.bearerToken
              
        else:
            token_ok = False
            while not token_ok:
                try:
                    print('Token vencido. Ingrese los datos')
                    username = input('Usuario: ')
                    password = input('Contraseña: ')
                    tk_dict = requestToken(username, password)
                    if tk_dict['access_token']:
                        token_ok = True
                except KeyError:
                    print('Error de token. Reingrese los datos')
            
            tk_obj = AuthenticationToken(token_dict = tk_dict)
            
            with open('token_file', 'wb') as token_f:
                pickle.dump(tk_obj,token_f)
                
            return self.bearerToken