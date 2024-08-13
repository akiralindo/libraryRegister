import tkinter as tk
from tkinter import ttk

class ViewAdd():
    def __init__(self):
        self.root = tk.Tk()
        self.tit("Biblioteca", 3, 0, "grey", "white", 20)
        self.tit("Adicionar Livro:", 1, 0, "#d3d3d3", "black", "9")
        self.inicializar()
    
    def inicializar(self):
        self.blankFrame(10)
        self.insert()
        self.blankFrame(30)
        self.bottomButtoms()
        self.blankFrame(20)
        self.root.mainloop()
    
    def tit(self, texto, height, width, bg, fg, font):
        self.titu = tk.Label(self.root, text=texto, height=height, width=width, bg=bg,  fg=fg, font=font)
        self.titu.pack(fill=tk.X)
    
    def blankFrame(self, h):
        b=tk.Frame(self.root, height=h)
        b.pack()
    
    def titulo(self):
        self.topFrame = tk.Frame(relief=tk.RAISED, height=100, bg="red")
        labelTitulo = tk.Label(self.topFrame, width=20, bg="red", text='Cadastro Veicular:')
        labelTitulo.pack()
        self.topFrame.pack(side=tk.TOP, fill=tk.X)
        
    def opc(self):
        container = tk.Frame(self.root)
        container.pack()
        labelFormato = tk.Label(container, width=20, text='Formato:')
        labelFormato.grid(column=0, row=0, padx=5, pady=5)
        self.gps = tk.BooleanVar()
        self.compBordo = tk.BooleanVar()
        chkBttn = tk.Checkbutton(container, text='GPS', width=20,
                                 variable=self.gps, anchor=tk.W)
        chkBttn.grid(column=1, row=0, padx=5, pady=5)

        chkBttn = tk.Checkbutton(container, text='Comp Bordo', width=20,
                                 variable=self.compBordo, anchor=tk.W)
        chkBttn.grid(column=1, row=1, padx=5, pady=5)
    
    def insert(self):
        cont=tk.Frame(self.root)
        cont.pack()
        a=tk.Label(cont, text='Nome:',justify="left")
        a.grid(sticky="W",padx=(5, 80),pady=(7,0),column=1, row=1)
        a=tk.Entry(cont, width=30)
        a.grid(column=2, row=1,padx=(10, 10))
        a=tk.Label(cont, text='Gênero:',justify="left")
        a.grid(sticky="W",pady=(7,0),padx=(5, 0),column=1, row=2)
        a=tk.Entry(cont, width=30)
        a.grid(column=2, row=2)
        a=tk.Label(cont, text='Editora:',justify="left")
        a.grid(sticky="W",pady=(7,0),padx=(5, 0),column=1, row=3)
        a=tk.Entry(cont, width=30)
        a.grid(column=2, row=3)
        a=tk.Label(cont, text='Autor:',justify="left")
        a.grid(sticky="W",pady=(7,0),padx=(5, 0),column=1, row=4)
        a=tk.Entry(cont, width=30)
        a.grid(column=2, row=4)

    def bottomButtoms(self,):
        cont=tk.Frame(self.root)
        cont.pack()
        b=tk.Button(cont, text="Salvar")
        b.grid(padx=(0,30),column=1, row=1)
        b=tk.Button(cont, text="Cancelar")
        b.grid(column=2, row=1)
        
run=ViewAdd()