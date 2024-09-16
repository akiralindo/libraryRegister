import tkinter as tk

class ViewUpdate(tk.Toplevel):
    def __init__(self, parent, book, update_callback):
        super().__init__(parent)
        self.book = book
        self.update_callback = update_callback
        self.title("Biblioteca", 2, 0, "grey", "white", ('Arial', 24))
        self.title("Atualizar:", 1, 0, "#d3d3d3", "black", ('Arial', 15))
        self.create_widgets()
        self.populate_fields()

    def title(self, texto, height, width, bg, fg, font):
        title = tk.Label(self, text=texto, height=height, width=width, bg=bg, fg=fg, font=font)
        title.grid(row=0, column=0, columnspan=2, sticky="ew")

    def create_widgets(self):
        self.fields = {
            "Nome": tk.StringVar(),
            "Gênero": tk.StringVar(),
            "Autor": tk.StringVar(),
            "Editora": tk.StringVar(),
            "Data de Publicação": tk.StringVar()
        }
        row = 1
        for field_name, var in self.fields.items():
            label = tk.Label(self, text=field_name)
            label.grid(row=row, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(self, textvariable=var)
            entry.grid(row=row, column=1, padx=10, pady=5, sticky="w")
            row += 1
        save_button = tk.Button(self, text="Salvar", command=self.save)
        save_button.grid(row=row, column=0, padx=10, pady=10, sticky="e")
        cancel_button = tk.Button(self, text="Cancelar", command=self.destroy)
        cancel_button.grid(row=row, column=1, padx=10, pady=10, sticky="w")

    def populate_fields(self):
        self.fields["Nome"].set(self.book[1])
        self.fields["Gênero"].set(self.book[2])
        self.fields["Autor"].set(self.book[3])
        self.fields["Editora"].set(self.book[4])
        self.fields["Data de Publicação"].set(self.book[5])

    def save(self):
        updated_values = {
            "name": self.fields["Nome"].get(),
            "genre": self.fields["Gênero"].get(),
            "author": self.fields["Autor"].get(),
            "publisher": self.fields["Editora"].get(),
            "date": self.fields["Data de Publicação"].get()
        }
        self.update_callback(self.book[0], updated_values)
        self.master.refresh_list()
        self.destroy()
