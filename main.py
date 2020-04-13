import requests
from secrets import env
from pprint import pprint

img = 'https://avatars2.githubusercontent.com/u/43324489?s=460&u=d27dca31efc4bad191e527943d2f2b47d9a55a07&v=4' #path to the image is located
api_key = env.API_KEY
request = requests.post("https://api.deepai.org/api/facial-expression-recognition",data={'image':img},headers={'api-key':api_key}) #request call, passing in img, and api key
data = request.json() #parsing request into json format
pprint(data) #print the data
