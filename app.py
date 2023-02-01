from flask import Flask, render_template

app = Flask(__name__)


# Criar primeira página
@app.route("/")
def pag_inicial():

    return render_template("index.html")

@app.route("/pedido")
def pag_pedido():

    return render_template("pedido.html")

@app.route("/pergunta")
def pag_pergunta():

    return render_template("pergunta.html")

# Criar a segunda página

# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)