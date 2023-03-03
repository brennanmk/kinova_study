from peewee import *

db = SqliteDatabase('study.db')
db.connect()

class Expirement(Model):
    user = IntegerField()
    plan1 = IntegerField()
    plan2 = IntegerField()
    preferance = IntegerField()
    class Meta:
        database = db

class dbController:
    def __init__(self) -> None:
        pass

    def createTable(self):
        db.create_tables([Expirement])

    def addEntry(self, usr, pln1, pln2, pref):
        Expirement.create(user=usr, plan1=pln1, plan2 = pln2, preferance=pref)

    def readDb(self):
        return Expirement.select().dicts()
    
if __name__ == '__main__':
    datab = dbController()
    datab.createTable()
    datab.addEntry(0,2,5,1)