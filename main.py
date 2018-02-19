#!/usr/bin/env python3

from tkinter import *

from threading import Thread

from other import main1

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
        train_button.grid(row = 3, column = 1)
        # Create a button
        render_button = Button(self, text = "Render", command = self.render_env)
        # Placing the button on my window
        render_button.grid(row = 3, column = 2)
        all_envs= [
        "Walker2d-v1",
        "Hopper-v1"
        ]
        variable = StringVar(self)
        env = OptionMenu(self, variable, *all_envs)
        env.grid(row = 0, column = 1)

    def train_env(self):
        thread = Thread(target = main1)
        thread.start() # This code will execute in parallel to the current code 
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
