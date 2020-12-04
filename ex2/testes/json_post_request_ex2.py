import requests
import json


def json_post_request_ex2(vetor):
    url = 'http://localhost:5000/algoritmo'
    headers = {'Content-Type': 'application/json'}
    parametro = json.dumps({'parametro': vetor})
    return requests.post(url, headers=headers, data=parametro)
