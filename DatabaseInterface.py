
import mysql.connector
from mysql.connector import errorcode
from DatabaseCredentials import *

class DatabaseInterface:
    def __init__(self):
        self.connection = []
        try:
            self.checkDenainaConnection()
        except:
            pass
        
    def __enter__(self):
        return 
    def checkDenainaConnection(self):
        try:
            cnx = mysql.connector.connect(user=denainaUsername, password=denainaPassword, database='SemanticNetworks', host=denainaHostname)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return False
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return False
            else:
                print(err)
                return False
        else:
            return True
            cnx.close()

    def insertArticleLink(self, connection):
        pass
    
    def insertArticleText(self, connection):
        pass
    
    def createDenainaConnection(self, denainaDatabase):
        self.connection = mysql.connector.connect(user=denainaUsername, password=denainaPassword, database=denainaDatabase, host=denainaHostname)
        
    def __exit__(self):
        self.connection.close()
    