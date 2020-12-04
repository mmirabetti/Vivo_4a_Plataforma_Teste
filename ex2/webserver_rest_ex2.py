from flask import Flask, request, jsonify
from algoritmo_ex2 import ex2_Vivo


app = Flask(__name__)


@app.route('/algoritmo', methods=["POST"])
def process():
    content = request.json
    parametro = content["parametro"]
    dict_resultado = ex2_Vivo(parametro)
    return jsonify({"resultado": dict_resultado})


if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port=5000,
            debug=True)
