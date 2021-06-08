from data import config
from datetime import datetime
import mysql.connector



class SQLighter:
    
    def __init__(self) -> None:
        self.myconn = mysql.connector.connect(
            host = config.HOST,
            user = config.USER,
            password = config.PASSWORD,
            database = config.DB
        )
        self.cur = self.myconn.cursor()

    def request_what_now(self):
        tdate = datetime(2021, 6, 18, 14, 50)
        #TODO: заменить tdate с ручного на строчку ниже
        # self.tdate = datetime.today()
        self.cur.execute("SELECT name, time_start "
                        "FROM schedule INNER JOIN event ON schedule.name_id = event.id "
                        "WHERE time_start <= '%s' AND time_end >= '%s'" % (tdate, tdate))
        self.result = self.cur.fetchall()
        return self.result
    
        
    def rq_try(self):
        self.cur.execute("SELECT name FROM event WHERE id=3")
        self.result = self.cur.fetchall()
        return self.result
    

    def close(self):
        self.myconn.close()

SQL = SQLighter()
