import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",         
    database="ciel2027",
    use_pure=True        
)

cursor = mydb.cursor()
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/v2/etudiants/<int:id>', methods=['GET' ])
def getEtudiant(id):
    req = f"SELECT * FROM etudiant WHERE idetudiant = {id}"
    print (req)
    try :
        cursor .execute(req)
        row = cursor. fetchone()
        etudiant = {
            "idetudiant": row[0],
            "nom": row[1],
            "prenom": row[2],
            "email": row[3],
            "telephone": row[4]
        }
        return jsonify(etudiant), 200
    except TypeError :
        return jsonify({'erreur':'id invalide'}), 404