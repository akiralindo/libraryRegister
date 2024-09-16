import mysql.connector
from datetime import datetime

class Model():

    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',    
            database='library',   
            user='root',  
            password='1234' 
        )
    
    def save_book(self, bookDetails):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            bookDetails["data_de_publicacao"] = datetime.strptime(bookDetails["data_de_publicacao"], "%Y-%m-%d").date()
            placeholders = ", ".join(["%s"] * len(bookDetails))
            insert_query = f"INSERT INTO books (nome, genero, autor, editora, data_de_publicacao) VALUES ({placeholders})"
            self.cursor.execute(insert_query, tuple(bookDetails.values()))
            self.connection.commit()
            self.cursor.close()
        
    def get_books(self):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            select_query = "SELECT * FROM books"
            self.cursor.execute(select_query)
            books = self.cursor.fetchall()
            self.cursor.close()
            return books
        
    def update_book(self, book_id, updated_values):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            update_query = """
                UPDATE books
                SET nome = %s, genero = %s, autor = %s, editora = %s, data_de_publicacao = %s
                WHERE id_books = %s
            """
            data = (
                updated_values["name"],
                updated_values["genre"],
                updated_values["author"],
                updated_values["publisher"],
                datetime.strptime(updated_values["date"], "%Y-%m-%d").date(),
                book_id
            )
            cursor.execute(update_query, data)
            self.connection.commit()
            cursor.close()
        
    def delete_book(self, book_id):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            delete_query = "DELETE FROM books WHERE id_books = %s"
            cursor.execute(delete_query, (book_id,))
            self.connection.commit()
            cursor.close()