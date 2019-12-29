import requests

url = 'http://localhost:8080/api'
r = requests.post(url, json = {"x" : ['I hate Brokeback Mountain']})
print(r.json())