"""
Example script for the invalid entry state
Author: rdbende
License: MIT license
"""


import tkinter as tk
from tkinter import ttk

import re


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Create widgets
        self.setup_widgets()

        # Bind the entries to validate methods
        self.bind_them()

    def setup_widgets(self):
        self.int_entry = ttk.Entry(self)
        self.int_entry.pack(padx=50, pady=(50, 25))

        self.color_entry = ttk.Entry(self)
        self.color_entry.pack(padx=50, pady=(25, 50))

    def bind_them(self):
        self.int_entry.bind("<FocusOut>", self.validate_int)
        self.int_entry.bind(
            "<FocusIn>", self.validate_int
        )  # Can't get the normal fosuced state
        self.int_entry.bind("<KeyRelease>", self.validate_int)

        self.color_entry.bind("<FocusOut>", self.validate_color)
        self.color_entry.bind(
            "<FocusIn>", self.validate_color
        )  # Can't get the normal fosuced state
        self.color_entry.bind("<KeyRelease>", self.validate_color)

    def validate_int(self, *_):
        """This method invalidates the entry if its content is not an integer"""
        if self.int_entry.get() == "":
            self.int_entry.state(["!invalid"])
        else:
            try:
                int(self.int_entry.get())
                self.int_entry.state(["!invalid"])
            except ValueError:
                self.int_entry.state(["invalid"])

    def validate_color(self, *_):
        """This method invalidates the entry if its content is not a 3 or 6 digit hex color code"""
        if self.color_entry.get() == "" or re.match(
            r"^#(?:[0-9a-fA-F]{3}){1,2}$", self.color_entry.get()
        ):
            self.color_entry.state(["!invalid"])
        else:
            self.color_entry.state(["invalid"])


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Invalid entry state example")

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
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

    root.mainloop()
