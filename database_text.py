create_client = """
                CREATE TABLE clients(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_user INTEGER,
                        fio VARCHAR(50),
                        email VARCHAR(50),
                        contact INTEGER,
                        order_id INTEGER,
                        payment_id INTEGER,
                        rebill_id INTEGER,
                        card_id INTEGER,
                        data_paid  VARCHAR(50),
                        data_will_pay VARCHAR(50),                      
                        check_ BOOLEAN
                        )
                """
clients_are_not_paid = """
                    CREATE TABLE clients_are_not_paid(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_user INTEGER,
                        date VARCHAR(50)
                        )
                       """                

insert_client = """
                INSERT INTO clients(
                    id_user,
                    fio,
                    email,
                    contact,
                    order_id,
                    payment_id,
                    rebill_id,
                    card_id,
                    data_paid,
                    data_will_pay,                      
                    check_ 
                )VALUES(?,?,?,?,?,?,?,?,?,?,?)
                """

insert_not_paid = """INSERT INTO clients_are_not_paid(
                    id_user,
                    date
                    )VALUES(?, ?)
                  """

update_client = "UPDATE clients set rebill_id=?, card_id=? WHERE id_user = ?"

