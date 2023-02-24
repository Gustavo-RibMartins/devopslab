from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Socorram-me, subi no onibus em Marrocos"