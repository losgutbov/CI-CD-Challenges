from flask import Flask


app = Flask(__name__)


@app.route("/teste/")
def teste():
    return "Testado!!"


@app.route("/")
def index():
    return "<p>Olá, Mundo!</p>"


if __name__ == "__main__":
    app.run()