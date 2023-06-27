# -*- coding: utf-8 -*-

import tkinter as tk

from shell import cli
from gui import App




def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":

    main()
