import sqlite3
from xlsxwriter import Workbook
from datetime import datetime
from database_text import*

class Database():
    def __init__(self):
        self.conn = sqlite3.connect("payment.db") 
        self.cursor = self.conn.cursor()
        ###################################
        self.query_client = create_client
        self.query_clients_are_not_paid = clients_are_not_paid 
        self.query_insert = insert_client
        self.query_insert_not_paid = insert_not_paid
        self.query_update = update_client

    def create_table_start(self):
        pass

    def create_table_client(self):
        self.cursor.execute(self.query_client)

        print("Clients table are created!")
    
    def create_table_not_paid(self):
        self.cursor.execute(self.query_clients_are_not_paid)

        print("Not paid table is created!")

    def insert_client(self, id, fio, email, contact, order_id, payment_id, rebill_id, card_id, data1, data2,  check):
        self.cursor.execute(self.query_insert, (id, fio, email, contact, order_id, payment_id, rebill_id, card_id, data1, data2, check, ))
        self.conn.commit()
        

    def update_client(self, rebill_id, card_id, id_user):
        self.query_update(self.query_update, (rebill_id, card_id, id_user, ))
        self.conn.commit()
    
    def insert_not_paid(self, id_user, data):
        self.cursor.execute(self.query_insert_not_paid, (id_user, data, ))
        self.conn.commit()
    

    def create_start_insert(self):
        self.cursor.execute()
        print("Start insert table is created!")

    def start_insert(self, id_user):
        self.cursor.execute()
        self.conn.commit()
     
    #############################
    def signal(self):
        pass
    ######### 


    def sql_2_excell(self, format: bool):
        pass        


if __name__ == "___main__":
    database = Database()
    database.create_table_client()
    database.create_table_not_paid()        