import tkinter as tk
from tkcalendar import DateEntry

class ViewAdd(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#e7e7e7")
        self.controller = controller
        self.title("Biblioteca", 2, 0, "grey", "white", ('Arial', 24))
        self.title("Adicionar:", 1, 0, "#d3d3d3", "black", ('Arial', 15))
        self.inicializar()

    def inicializar(self):
        self.blankFrame(10)
        self.insertBook()
        self.blankFrame(30)
        self.bottomButtoms()
        self.blankFrame(20)

    def title(self, texto, height, width, bg, fg, font):
        titulo = tk.Label(self, text=texto, height=height, width=width, bg=bg, fg=fg, font=font)
        titulo.pack(fill=tk.X)

    def blankFrame(self, h):
        blankFrame = tk.Frame(self, height=h, bg="#e7e7e7")
        blankFrame.pack()
    
    def save_book(self):
        self.book_details = {}
        self.book_details['Nome'] = self.nome_entry.get()
        self.book_details['Gênero'] = self.genero_entry.get()
        self.book_details['Autor'] = self.autor_entry.get()
        self.book_details['Editora'] = self.editora_entry.get()
        self.book_details['Data de Publicação'] = self.data_entry.get()
        self.controller.saveBook(self.book_details)

    def insertBook(self):
        cont = tk.Frame(self,bg=self['bg'])
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
        self.data_entry = DateEntry(cont, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.data_entry.grid(sticky="W", padx=(0, 10), pady=(9, 0), column=2, row=6)
        
    def getDataEntryValue(self):
        return self.data_entry.get()
    
    def bottomButtoms(self):
        cont = tk.Frame(self, bg=self['bg'])
        cont.pack(pady=(20, 0))
        salvar_button = tk.Button(cont, text="Salvar", command=self.save_book, width=14, height=2, bg="grey", fg="white")
        salvar_button.grid(padx=(0, 30), column=0, row=0)
        cancelar_button = tk.Button(cont, text="Voltar", command=lambda: self.controller.show_frame("StartPage"), bg="grey", width=14, height=2, fg="white")  # Mudar cor do botão
        cancelar_button.grid(column=1, row=0)
        