from flask import Flask, request, jsonify
from textblob import TextBlob
import os

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
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
