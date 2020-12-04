# Teste para novos Desenvolvedores
## Telefônica Vivo - 4th Plataforma – Versão 2.0 - 2020
## Exercício 2

### Enunciado
Transforme o algoritmo anterior (do Exercício 1) em uma API Rest. Você receberá como parâmetro uma lista com os valores de An e deverá retornar a saída do algoritmo no formato JSON.

### Considerações
* Foi utilizado o framework Flask para implementação local do webserver que disponibilizaria a API Rest / endpoints
* Também foram usado o pacote "request", "json" e o "jsonify", este último para geração da resposta em JSON a partir da estrutura de dados dicionário da linguagem Python.
* Considerando os pacotes de requisitos, foi utilizada um ambiente virtual (virtual environment), para isolamento do sistema host.

### Requisitos
Pacotes Flask, request, e jsonify. Para os testes funcionais, o único requisito é o pacote pytest.

### Coding style
O código foi desenvolvido usando as regras PEP8

### Execução
Para ativação do ambiente virtual, basta executar o comando:
```shell
. apis/bin/activate
```

Para desaativação do ambiente virtual, basta executar o comando:
```shell
deactivate
```
Para ativação do webserver, basta executar o comando:
```shell
python webserver.rest_ex2.py
```

Para testes isolado, foi fornecida uma função em Python para acesso do endpoint disponibilizado pelo webserver, através do método POST. Basta modificar a função com os dados desejados, e executar o comando:

```shell
python json_post_request_ex2.py
```

### Testes funcionais
Para a realização dos testes, basta executar o comando
```shell
pytest testes
```
