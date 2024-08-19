import tkinter as tk
from tkinter import font as tkfont
from startPage import StartPage
from viewAdd import ViewAdd  
import controller as ct

class ViewMain(tk.Tk):
    def __init__(self): 
        tk.Tk.__init__(self)
        self.controller = ct.Controller()
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, ViewAdd):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def saveBook(self, book_details):
        self.controller.saveBook(book_details)

if __name__ == "__main__":
    app = ViewMain()
    app.geometry('360x400')
    app.mainloop()