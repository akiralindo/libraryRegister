import tkinter as tk
from startPage import StartPage
from viewAdd import ViewAdd  
from viewList import ViewList
import controller as ct

class ViewMain(tk.Tk):
    def __init__(self): 
        super().__init__()
        self.controller = ct.Controller()
        container = tk.Frame(self)
        self.view_list = ViewList(self, self.controller)
        self.controller.view_list = self.view_list
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, ViewAdd, ViewList):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def save_book(self, book_details):
        self.controller.save_vook(book_details)
    
    def get_book(self):
        return self.controller.get_book()
    
    def update_book(self, book_id, updated_book):
        self.controller.update_book(book_id, updated_book)
        
    def delete_book(self, book_id):
        self.controller.delete_book(book_id)
        
    def refresh_list(self):
        self.view_list.refresh_list()

if __name__ == "__main__":
        app = ViewMain()
        app.geometry('360x400')
        app.mainloop()