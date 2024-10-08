import tkinter as tk
from tkcalendar import DateEntry

class ViewAdd(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#e7e7e7")
        self.controller = controller
        self.title("Biblioteca", 2, 0, "grey", "white", ('Arial', 24))
        self.title("Adicionar:", 1, 0, "#d3d3d3", "black", ('Arial', 15))
        self.init()

    def init(self):
        self.blank_frame(10)
        self.insert_book()
        self.blank_frame(30)
        self.bottom_buttoms()
        self.blank_frame(20)

    def title(self, texto, height, width, bg, fg, font):
        title = tk.Label(self, text=texto, height=height, width=width, bg=bg, fg=fg, font=font)
        title.pack(fill=tk.X)

    def blank_frame(self, h):
        blankFrame = tk.Frame(self, height=h, bg="#e7e7e7")
        blankFrame.pack()
    
    def save_book(self):
        self.book_details = {}
        self.book_details['Nome'] = self.nome_entry.get()
        self.book_details['Gênero'] = self.genero_entry.get()
        self.book_details['Autor'] = self.autor_entry.get()
        self.book_details['Editora'] = self.editora_entry.get()
        self.book_details['data_de_publicacao'] = self.data_entry.get()
        self.controller.saveBook(self.book_details)
        self.clear_entries() 
        
    def insert_book(self):
        cont = tk.Frame(self, bg="#e7e7e7")
        cont.pack()
        labels = [
            "Nome:",
            "Gênero:",
            "Autor:",
            "Editora:"
        ]
        self.entries = {}
        for i, label_text in enumerate(labels):
            label = tk.Label(cont, text=label_text, justify="left", bg="#e7e7e7")
            label.grid(sticky="W", padx=(5, 10), pady=(9, 0), column=1, row=i+1)
            entry = tk.Entry(cont, width=25, font=("Arial",12))
            entry.grid(sticky="W", padx=(0, 10), pady=(9, 0), column=2, row=i+1)
            self.entries[label_text] = entry
        self.nome_entry = self.entries["Nome:"]
        self.genero_entry = self.entries["Gênero:"]
        self.autor_entry = self.entries["Autor:"]
        self.editora_entry = self.entries["Editora:"]
        self.data_label = tk.Label(cont, text="Data de Publicação:", justify="left", bg="#e7e7e7")
        self.data_label.grid(sticky="W", padx=(5, 10), pady=(9, 0), column=1, row=6)
        self.data_entry = DateEntry(cont, width=12, background="darkblue", foreground="white", borderwidth=2, date_pattern='yyyy-mm-dd')
        self.data_entry.grid(sticky="W", padx=(0, 10), pady=(9, 0), column=2, row=6)
        
    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.data_entry.set_date('')
    
    def get_data_entry_value(self):
        return self.data_entry.get()
    
    def bottom_buttoms(self):
        cont = tk.Frame(self, bg="#e7e7e7")
        cont.pack(pady=(20, 0))
        save_button = tk.Button(cont, text="Salvar", command=self.save_book, width=14, height=2, bg="grey", fg="white")
        save_button.grid(padx=(0, 30), column=0, row=0)
        cancel_button = tk.Button(cont, text="Voltar", command=lambda: self.controller.show_frame("StartPage"), bg="grey", width=14, height=2, fg="white")
        cancel_button.grid(column=1, row=0)