from flask import Flask, jsonify
import mysql.connector
mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "ciel2027"
)
cursor = mydb.cursor()
app = Flask(__name__)

@app.route('/v1/etudiants/<int:id>', methods=['GET'])
def getEtudiant(id):
    req = f"SELECT * FROM etudiant WHERE idetudiant = {id}"
    print(req)
    cursor.execute(req)
    row = cursor.fetchone()  
    if not row:
        return jsonify({"message": "Étudiant non trouvé"}), 404

    etudiant = {
        "idetudiant": row[0],
        "nom": row[1],
        "prenom": row[2],
        "email": row[3],
        "telephone": row[4]
    }
    return jsonify(etudiant), 200  

if __name__ == '__main__':
    app.run(debug=True)