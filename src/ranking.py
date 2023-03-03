import pandas
from database import dbController

class rank:
    def __init__(self):
        db = dbController()
        data = db.readDb()

        df = pandas.DataFrame(data)   
        df = df.set_index("id")
        print(df)

if __name__=='__main__':
    rank()