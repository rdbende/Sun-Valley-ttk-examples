"""
Example script for a nice calculator
Author: rdbende
License: GNU GPLv3 license
"""


import tkinter as tk
from functools import partial
from tkinter import ttk


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2, 3]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index + 1, weight=1)

        self.result = tk.StringVar(value="")

        # Create widgets
        self.setup_widgets()

    def setup_widgets(self):
        self.label = ttk.Label(
            self, anchor="e", textvariable=self.result, font=("-size", 15), padding=5
        )
        self.label.grid(row=0, column=0, columnspan=4, sticky="ew")

        for index, key in enumerate("147C2580369=+-*/"):
            ttk.Button(
                self,
                text=key,
                style="Accent.TButton" if key == "=" else "TButton",
                command=partial(self.button_pressed, key),
            ).grid(row=index % 4 + 1, column=index // 4, sticky="nsew", padx=2, pady=2)

    def button_pressed(self, key):
        if key == "C":
            self.result.set("")
        elif key == "=":
            self.result.set(str(round(eval(self.result.get()))))
        else:
            self.result.set(self.result.get() + key)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("300x300")
    root.attributes("-topmost", True)  # It stays always on top of other windows

    # Simply set the theme
    root.tk.call("source", "sun-valley.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

    root.mainloop()
