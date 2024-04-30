import tkinter as tk


class StringEntry(tk.Entry):
    def __init__(self, master=None, width=30, **kwargs):
        super().__init__(master, **kwargs)
        self.width = width
        self.config(width=self.width)
        self.submit_button = tk.Button(
            master, text="Submit", command=self.validate_input)
        self.submit_button.pack(side=tk.LEFT)

    def validate_input(self):
        value = self.get()
        if not isinstance(value, str):
            # Si no es una cadena, eliminamos el último caracter ingresado
            self.delete(len(value) - 1, tk.END)
