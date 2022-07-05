"""A simple but kinda useless calculator"""

import tkinter as tk
from functools import partial
from tkinter import ttk

import sv_ttk


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        # Make the app responsive
        for index in range(4):
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
                style="TButton" if key != "=" else "Accent.TButton",
                command=partial(self.button_pressed, key),
            ).grid(row=index % 4 + 1, column=index // 4, sticky="nsew", padx=2, pady=2)

    def button_pressed(self, key):
        if key == "C":
            self.result.set("")
        elif key == "=":
            self.result.set(str(round(eval(self.result.get()))))
        else:
            self.result.set(self.result.get() + key)


def main():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("300x300")
    root.attributes("-topmost", True)  # Make it be always-on-top

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
