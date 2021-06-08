from datetime import datetime
import mysql.connector


class SQLighter:
    
    def __init__(self) -> None:
        self.myconn = mysql.connector.connect(
            host = 'localhost',
            user = 'dmartinchick',
            password = 'samsungLX40',
            database = 'svarog2021'
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
        t1 = datetime(2021, 6, 18, 15, 30)
        self.cur.execute("SELECT id FROM schedule WHERE time_start = '%s'" % (t1))
        self.result = self.cur.fetchall()
        return self.result
    

    def close(self):
        self.myconn.close()

SQL = SQLighter()


# print(datetime.now())
# print(SQL.rq_try())
print(SQL.request_what_now())