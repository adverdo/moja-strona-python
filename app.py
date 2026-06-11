from flask import Flask, render_template

app = Flask(__name__)

# Główna strona (wczytuje plik index.html z folderu templates)
@app.route("/")
def home():
    return render_template("index.html")

# Dodatkowa podstrona O Mnie
@app.route("/o-mnie")
def o_mnie():
    return "<h2>Tutaj w przyszłości też możesz dodać ładny szablon HTML!</h2>"

@app.route("/sekret")
def sekret():
    return render_template("sekret.html")
    
if __name__ == "__main__":
    app.run(debug=True)
