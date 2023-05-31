import sys
import tkinter as tk
from tkinter import filedialog
import ManualGui
import Monitor

WIDTH = 600
HEIGHT = 720


class MonitorGui:
    def __init__(self, t):
        # self.monitor = m
        self.t = t
        # Monitor.Monitor.auto()
        self.moni = tk.Tk()
        self.run = True
        self.manu_gui = None  # ManualGui.ManualGui()
        self.moni.geometry(f"{WIDTH}x{HEIGHT}")
        self.moni.title("Monitor Representation")
        self.display_change = tk.Label(self.moni, bg='green')

        button_exit = tk.Button(self.moni, text="EXIT", command=self.moni.quit)
        button_exit.config(width=10, height=2)
        button_exit.place(x=0, y=0)

        button_manual = tk.Button(self.moni, text="Manual", command=lambda: self.show_manual_screen())
        button_manual.pack(pady=10)
        button_manual.config(width=10, height=2)
        button_manual.place(x=80, y=0)

        self.frame = tk.Frame(self.moni)
        self.scroll = tk.Scrollbar(self.frame)
        self.screen = tk.Listbox(self.frame, width=500, height=400, yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.screen.yview)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.frame.place(x=10, y=40, width=500, height=600)
        self.screen.pack(pady=15)

        self.change_list = self.read_change()
        # self.display_change()
        # self.read_change()
        for change in self.change_list:
            self.screen.insert(tk.END, change)
        self.moni.mainloop()

    def stop(self):
        self.monitor.run = False

    def display_change(self):
        for change in self.change_list:
            self.screen.insert(tk.END, change)
        self.screen.after(1000, self.display_change())

    def read_change(self):
        with open("StatusLog.txt", 'r') as f:
            change = f.readlines()
        f.close()
        # self.change_list = change
        # self.screen.after(self, 100, self.read_change())
        return change

    def show_manual_screen(self):
        self.manu_gui = ManualGui.ManualGui().manual()

    # def refresh(self):
    #     self.moni.destroy()
    #     self.__init__()

    # def exit(self):
    #     self.monitor.run = False
