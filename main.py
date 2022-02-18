import os
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/calculadora', methods=['POST', 'GET'])
def calculadora():
    valor1 = request.form["valor1"]
    valor2 = request.form["valor2"]
    operacao = request.form["operacao"]

    v1 = int(valor1)
    v2 = int(valor2)

    match operacao:
        case "soma" | "+":
            resultado = v1 + v2
        case "subtracao" | "-":
            resultado = v1 - v2
        case "multiplicacao" | "*":
            resultado = v1 * v2
        case "divisao" | "/":
            resultado = v1 / v2

    return str(resultado)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
