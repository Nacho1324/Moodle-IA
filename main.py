from flask import Flask, request, jsonify
import pandas as pd
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return "IA de Moodle funcionando ✅"

@app.route('/analizar', methods=['POST'])
def analizar():
    data = request.get_json()
    respuesta = data.get("respuesta", "")
    analisis = TextBlob(respuesta)
    sentimiento = analisis.sentiment.polarity

    if sentimiento > 0.2:
        resultado = "Buena respuesta"
    elif sentimiento < -0.2:
        resultado = "Deficiente"
    else:
        resultado = "Neutra"

    return jsonify({"evaluacion": resultado})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
