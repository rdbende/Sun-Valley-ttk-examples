import re
import tkinter as tk
from tkinter import ttk

import sv_ttk


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        # Create widgets
        self.setup_widgets()

        # Bind the entries to the validator methods
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
        """
        This method invalidates the entry if its content is not an integer
        """

        if self.int_entry.get() == "":
            self.int_entry.state(["!invalid"])
        else:
            try:
                int(self.int_entry.get())
                self.int_entry.state(["!invalid"])
            except ValueError:
                self.int_entry.state(["invalid"])

    def validate_color(self, *_):
        """
        This method invalidates the entry if its content is not a 3 or 6 digit hex color code
        """

        if self.color_entry.get() == "" or re.match(
            r"^#(?:[0-9a-fA-F]{3}){1,2}$", self.color_entry.get()
        ):
            self.color_entry.state(["!invalid"])
        else:
            self.color_entry.state(["invalid"])


def main():
    root = tk.Tk()
    root.title("Invalid entry state example")

    sv_ttk.set_theme("dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    root.update_idletasks()  # Make sure every screen redrawing is done

    width, height = root.winfo_width(), root.winfo_height()
    x = int((root.winfo_screenwidth() / 2) - (width / 2))
    y = int((root.winfo_screenheight() / 2) - (height / 2))

    # Set a minsize for the window, and place it in the middle
    root.minsize(width, height)
    root.geometry(f"+{x}+{y}")

    root.mainloop()


if __name__ == "__main__":
    main()
