from os import close

from marshmallow.fields import Int
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

    def close(self):
        self.myconn.close()

    # Методы извлечения данных
    def what_now(self):
        self.tdate = datetime(2021, 6, 18, 19, 40)
        #TODO: заменить tdate с ручного на строчку ниже
        # self.tdate = datetime.today()
        self.cur.execute("SELECT name, time_start, time_end, address, contains "
                        "FROM schedule INNER JOIN event ON schedule.name_id = event.id "
                        "WHERE time_start <= '%s' AND time_end >= '%s'" % (self.tdate, self.tdate))
        self.result = self.cur.fetchall()
        return self.result
        close(self)

    #TODO: реализовать функцию result_info
    def result_info(self):
        pass

    #TODO: Реализовать функцию event_info
    def event_info(self, event_name):
        """Принимает название конкурса и возвращает подробную информацию о конкурсе

        Args:
            event_name ([type]): Название конкурса
        """
        pass


    def find_date_start(self):
        self.cur.execute("SELECT MIN(time_start) FROM schedule;")
        self.result = self.cur.fetchone()
        return self.result[0].strftime('%d.%m %H:%M')


    def find_date_end(self):
        self.cur.execute("SELECT MAX(time_end) FROM schedule;")
        self.result = self.cur.fetchone()
        return self.result[0].strftime('%d.%m %H:%M')
    

    def get_users(self):
        self.cur.execute("SELECT user_id FROM users;")
        self.result = self.cur.fetchall()
        return self.result
        close(self)
        
    # Методы добавления данных
    def set_users(self, user):
        """Добавляет пользователя в БД в таблицу Users

        Args:
            user (Int): Индитификатор пользователя
        """
        self.cur.execute(f"INSERT INTO users(user_id) VALUES ({user});")
        self.myconn.commit()
        

SQL = SQLighter()
