#!/usr/bin/env python3

from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.pack(fill = BOTH, expand = True)

        # Title of window
        self.master.title('Automated Gait Generation for Simulated Machines')
        # Create a button
        train_button = Button(self, text = "Train", command = self.train_env)
        # Placing the button on my window
        train_button.grid(row = 1, column = 0)
        # Create a button
        render_button = Button(self, text = "Render", command = self.render_env)
        # Placing the button on my window
        render_button.grid(row = 1, column = 5)

    def train_env(self):
        exit()

    def render_env(self):
        exit()


def main():
    root = Tk()
    # size of the window
    root.geometry("400x300")
    app = Window(root)
    root.mainloop()
    return

if __name__ == '__main__':
    main()
