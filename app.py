from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    resultado = None
    media = None    

    nota1 = request.args.get('nota1')
    nota2 = request.args.get('nota2')

    if nota1 and nota2:  
        nota1 = float(nota1)
        nota2 = float(nota2)

        media = (nota1 + nota2) / 2

    return jsonify(media)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)