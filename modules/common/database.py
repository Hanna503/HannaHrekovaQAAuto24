import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'h://Робота//Git//HannaHrekovaQAAuto24/' + r'//become_qa_auto.db')
        self.cursor = self.connection.cursor()

        self.create_table()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f'Connected successfully. SQLite Database Version is: {record}')

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders\
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
   
    def create_table(self):
        with self.connection:
            self.connection.execute('''CREATE TABLE IF NOT EXISTS data (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    value TEXT NOT NULL
                                )''')
            
    def check_table_exists(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT name FROM sqlite_master WHERE type='table' AND name='data';
        ''')
        if cursor.fetchone() is None:
            self.create_table()
    
    def add_data(self, value):
        if not isinstance(value, (int, float, str, bool, list, dict)):
            raise ValueError("Unsupported data type")
        with self.connection:
            self.connection.execute("INSERT INTO data (value) VALUES (?)", (str(value),))
        return True
    
    def update_data(self, data_id, value):
        if not isinstance(value, (int, float, str, bool, list, dict)):
            raise ValueError("Unsupported data type")
        with self.connection:
            self.connection.execute("UPDATE data SET value = ? WHERE id = ?", (str(value), data_id))
        return True
    
    def get_data(self):
        cursor = self.connection.execute("SELECT * FROM data")
        return cursor.fetchall()
    
    def add_large_values(self, value):
        self.add_data(value)
        return True
    
    def get_data_by_id(self, data_id):
        cursor = self.connection.execute("SELECT * FROM data WHERE id = ?", (data_id,))
        return cursor.fetchone()
    
    def avoid_duplicates(self, value):
        cursor = self.connection.execute("SELECT * FROM data WHERE value = ?", (str(value),))
        if cursor.fetchone():
            return False
        self.add_data(value)
        return True
    
    def delete_data(self, data_id):
        with self.connection:
            self.connection.execute("DELETE FROM data WHERE id = ?", (data_id))
        return True

    def clear_table(self):
        with self.connection:
            self.connection.execute("DELETE FROM data")
            self.connection.execute("DELETE FROM sqlite_sequence WHERE name='data'")
        return True