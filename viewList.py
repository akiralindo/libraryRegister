import tkinter as tk
from viewUpdate import ViewUpdate

class ViewList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#e7e7e7")
        self.controller = controller
        self.title("Biblioteca", 2, 0, "grey", "white", ('Arial', 24))
        self.title("Livros:", 1, 0, "#d3d3d3", "black", ('Arial', 15))
        self.center_frame = tk.Frame(self, bg="#e7e7e7")
        self.center_frame.pack(expand=True, fill="both")
        self.canvas = tk.Canvas(self.center_frame, bg="#e7e7e7", height=240)
        self.scrollbar = tk.Scrollbar(self.center_frame, orient="vertical", command=self.canvas.yview)
        self.frame = tk.Frame(self.canvas, bg="#e7e7e7")
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", anchor="center", padx=(75,0))
        self.scrollbar.pack(side="right", fill="y")
        self.frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        self.bind_mouse_scroll()
        self.inicializar()
        self.refresh_list()

    def inicializar(self):
        self.populate_list()
        self.blank_frame(5)
        self.bottom_buttoms()
        self.blank_frame(10)
        self.refresh_list()
    
    def populate_list(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.books = self.controller.get_book()
        if self.books:
            for book in self.books:
                item_frame = tk.Frame(self.frame, bg="#e7e7e7", height=50)
                item_frame.pack(fill="x", pady=2)
                item_label = tk.Label(item_frame, text=f"{book[1]}", bg="#e7e7e7", font=("Arial", 12))
                item_label.pack(side="left", fill="x", expand=True)
                item_button = tk.Button(item_frame, text="Detalhes", bg="#d3d3d3", command=lambda book=book: self.open_item_window(book))
                item_button.pack(side="right", padx=(3, 0))
                delete_button = tk.Button(item_frame, text="Deletar", bg="#d3d3d3", command=lambda book_id=book[0]: self.delete_book(book_id))
                delete_button.pack(side="right", padx=(70, 0))
        else:
            tk.Label(self.frame, text="Nenhum livro disponível", bg="#e7e7e7").pack()
    
    def refresh_list(self):
        self.populate_list()

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.config(width=self.center_frame.winfo_width())
        self.frame.config(width=self.canvas.winfo_width())
        
    def bind_mouse_scroll(self):
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

    def on_mouse_wheel(self, event):
        if event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")

    def title(self, texto, height, width, bg, fg, font):
        title = tk.Label(self, text=texto, height=height, width=width, bg=bg, fg=fg, font=font)
        title.pack(fill=tk.X)
    
    def blank_frame(self, h):
        blankFrame = tk.Frame(self, height=h, bg="#e7e7e7")
        blankFrame.pack()
    
    def bottom_buttoms(self):
        cont = tk.Frame(self, bg=self['bg'])
        cont.pack(pady=(5, 0))
        save_button = tk.Button(cont, text="Atualizar", command=self.refresh_list, width=14, height=2, bg="grey", fg="white")
        save_button.grid(padx=(0, 30), column=0, row=0)
        cancel_button = tk.Button(cont, text="Voltar", command=lambda: self.controller.show_frame("StartPage"), bg="grey", width=14, height=2, fg="white")
        cancel_button.grid(column=1, row=0)
        
    def open_item_window(self, book):
        def update_book(book_id, updated_values):
            self.master.master.update_book(book_id, updated_values)
            self.refresh_list()
        ViewUpdate(self, book, update_book)
    
    def delete_book(self, book_id):
        self.master.master.delete_book(book_id)
        self.refresh_list()
