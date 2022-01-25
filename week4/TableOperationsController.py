import UserCreateController
from datetime import datetime
import sqlite3
class TableCreate:
    def __init__(self):
        self.TABLE = datetime.now().strftime(f"%b_%d_%Y_%H_%M_%S")
        self.query = f'''CREATE TABLE {self.TABLE}
        (
            SQ_USER_NO      INTEGER PRIMARY KEY AUTOINCREMENT,
            USERNAME        TEXT,
            EMAIL           TEXT,
            FULL_NAME       TEXT,
            EMAIL_USER_IK   INTEGER,
            USERNAME_IK     INTEGER,
            B_YEAR          TEXT,
            B_MONTH         TEXT,
            B_DAY           TEXT,
            COUNTRY         TEXT,
            FL_ACTIVE       INTEGER
        );
        
        '''
        self.insertStatements = f'''
            INSERT INTO {self.TABLE} 
            (
            USERNAME,
            EMAIL,
            FULL_NAME,
            EMAIL_USER_IK,
            USERNAME_IK,
            B_YEAR,
            B_MONTH,
            B_DAY,
            COUNTRY,
            FL_ACTIVE
            )
            VALUES
            (?,?,?,?,?,?,?,?,?,?)
        '''

    def Insertion(self,dbName,jsonFile):
        users = UserCreateController.UserCreate(jsonFile)
        allUsers = users.jsonGetter()
        db = sqlite3.connect(dbName)
        cursor = db.cursor()
        cursor.execute(self.query)
        for user in allUsers:
            cursor.execute(self.insertStatements,(
                user.username,
                user.email,
                user.fullName,
                user.emailuserlk,
                user.usernamelk,
                user.bYear,
                user.bMonth,
                user.bDay,
                user.country,
                user.isActive
                ))
        db.commit()
