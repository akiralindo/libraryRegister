import tkinter as tk

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#e7e7e7")
        self.controller = controller
        self.title("Biblioteca", 2, 0, "grey", "white", ('Arial', 24))
        self.title("Selecione:", 1, 0, "#d3d3d3", "black", ('Arial', 15))

        button1 = tk.Button(self, width=13, height=2, bg="#d3d3d3", font=("Arial",20), text="Adicionar Livro",
                            command=lambda: controller.show_frame("ViewAdd"))
        button1.pack(pady=(30, 0))
        button2 = tk.Button(self, width=13, height=2, bg="#d3d3d3", font=("Arial",20), text="Ver Livros",
                            command=lambda: controller.show_frame("ViewAdd"))
        button2.pack(pady=(15, 0))
        
    def title(self, texto, height, width, bg, fg, font):
        titulo = tk.Label(self, text=texto, height=height, width=width, bg=bg, fg=fg, font=font)
        titulo.pack(fill=tk.X)