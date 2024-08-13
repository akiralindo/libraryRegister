from model import Model

class Controller():
    def __init__(self):
        self.model=Model()
    def saveBook(self, book_details):
        self.model.saveBook(book_details)