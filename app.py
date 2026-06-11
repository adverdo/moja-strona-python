import os
from flask import Flask, render_template

base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def home():
    # TEST SZPIEGOWSKI: Wypisujemy w logach, co widzi serwer
    print(f"--- KATALOG BAZOWY: {base_dir} ---")
    try:
        print(f"Zawartosc katalogu bazowego: {os.listdir(base_dir)}")
        if os.path.exists(template_dir):
            print(f"Zawartosc folderu templates: {os.listdir(template_dir)}")
        else:
            print("Blad: Folder 'templates' NIE ISTNIEJE w tej lokalizacji!")
    except Exception as e:
        print(f"Blad skanowania: {e}")
        
    return render_template("index.html")

@app.route("/o-mnie")
def o_mnie():
    return "<h2>Tutaj w przyszłości też możesz dodać ładny szablon HTML!</h2>"

@app.route("/sekret")
def sekret():
    return render_template("sekret.html")

if __name__ == "__main__":
    app.run(debug=True)
