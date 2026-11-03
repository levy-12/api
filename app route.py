import mysql.connector
from flask import Flask, app, jsonify
mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "ciel2027"
)
app = Flask(__name__)
cursor = mydb.cursor()

@app.route('/etudiants/', methods=['GET'])
def getEtudiants():
    etudiants = ()
    request = "SELECT * FROM etudiant"
    cursor.execute(request)
    result = cursor.fetchall()
    for row in result:
        etudiant = {
            "idetudiant": row[0],
            "nom": row[1],
            "prenom": row[2],
            "email": row[3],
            "telephone": row[4]
        }
        etudiants.append(etudiant)
    return jsonify(etudiants), 201
