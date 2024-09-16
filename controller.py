from model import Model

class Controller():
    def __init__(self):
        self.model = Model()

    def save_book(self, book_details):
        self.model.save_book(book_details)
        self.view_list.refresh_list()

    def get_book(self):
        return self.model.get_books()

    def update_book(self, book_id, updated_values):
        self.model.update_book(book_id, updated_values)
        self.view_list.refresh_list()
        
    def delete_book(self, book_id):
        self.model.delete_book(book_id)
        self.view_list.refresh_list()