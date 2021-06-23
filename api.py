from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def API():
    data = request.get_json()
    predicao = np.array2string(modelo.predict(data))
    return jsonify(predicao)

if __name__ == '__main__':
    modelfile = 'modelo_vinho.pickle'
    modelo = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0',port=8080)
