import requests
import json

url = 'http://localhost:5000/algoritmo'
headers = {'Content-Type': 'application/json'}
parametro = json.dumps({'parametro': [0, 1, 2, 3, 4, 5]})

response = requests.post(url, headers=headers, data=parametro)

print(response.json())
