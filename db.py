import mysql.connector

class Database:

    def __init__(self, host, user, password, database):
        self.host =host
        self.user = user
        self.password = password
        self.database = database

    def __connect(self):
         connector = mysql.connector.connect(
             host = self.host,
             user = self.user,
             password = self.password,
             database = self.database)
         return connector
         