from flask import Flask

app = Flask(__name__)
        

@app.route('/')
def home():
    return 'Page d\'accueil'

@app.route('/etudiant/')
def about():
    return 'Page etudiant'


if __name__ == "__main__":
    app.run(debug=True)