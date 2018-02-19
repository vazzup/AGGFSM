#!/usr/bin/env python3

from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

def main():
    root = Tk()
    app = Window(root)
    root.mainloop()
    return

if __name__ == '__main__':
    main()
