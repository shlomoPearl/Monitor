import math
import sys
import threading
import time
import tkinter as tk
from queue import Queue
from threading import Thread
import Monitor

import Monitor

WIDTH = 600
HEIGHT = 720
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 60 * SECONDS_IN_MINUTE
global auto_hour
global auto_minute
global auto_seconds

global manual_hour1
global manual_minute1
global manual_seconds1
global manual_year1
global manual_month1
global manual_day1

global manual_hour2
global manual_minute2
global manual_seconds2
global manual_year2
global manual_month2
global manual_day2


class GuiMonitor:

    def __init__(self):
        self.Monitor = Monitor.Monitor()
        self.read_change = None
        self.manual_thread = None
        self.manual_win = None
        self.auto_win = None
        self.auto_thread = None
        self.run = True
        self.queue = Queue()
        self.moni = tk.Tk()
        self.moni.geometry(f"{WIDTH}x{HEIGHT}")
        self.moni.title("Monitor Representation")
        self.display_change = tk.Label(self.moni, bg='green')
        roll = tk.Scrollbar(self.moni)
        roll.pack(side=tk.RIGHT, fill=tk.Y)

        button_exit = tk.Button(self.moni, text="EXIT", command=lambda: sys.exit())
        button_exit.config(width=10, height=2)
        button_exit.place(x=0, y=0)

        button_auto = tk.Button(self.moni, text="Auto", command=self.auto)
        button_auto.pack(pady=10)
        button_auto.config(width=10, height=2)
        button_auto.place(x=80, y=0)

        button_manual = tk.Button(self.moni, text="Manual", command=self.manual)
        button_manual.pack(pady=10)
        button_manual.config(width=10, height=2)
        button_manual.place(x=160, y=0)

        self.moni.mainloop()

    def close_sub_win(self):
        if self.auto_win is not None:
            self.auto_win.destroy()
        if self.manual_win is not None:
            self.manual_win.destroy()

    def read_auto_change(self):
        try:
            with open('statusLog.txt', 'r') as f:
                change = f.readlines()
                self.display_change.config(text=change)
            f.close()
        except FileNotFoundError:
            print("there is no change in services yet")
            time.sleep(30)

    def start_manual(self):
        # event1 inputs
        global manual_hour1
        if not manual_hour1.get().isnumeric():
            h1 = 0
        else:
            h2 = int(manual_hour1.get())
        global manual_minute1
        if not manual_minute1.get().isnumeric():
            min1 = 0
        else:
            min1 = int(manual_minute1.get())
        global manual_seconds1
        if not manual_seconds1.get().isnumeric():
            s1 = 0
        else:
            s1 = int(manual_seconds1.get())
        global manual_year1
        if not manual_year1.get().isnumeric():
            y1 = 0
        else:
            y1 = int(manual_year1.get())
        global manual_month1
        if not manual_month1.get().isnumeric():
            mon1 = 0
        else:
            mon1 = int(manual_month1.get())
        global manual_day1
        if not manual_day1.get():
            d1 = 0
        else:
            d1 = int(manual_day1.get())
        event1 = f"{y1}-{mon1}-{d1} {h1}:{min1}:{s1}"
        # event2 input
        global manual_hour2
        if not manual_hour2.get().isnumeric():
            h2 = 0
        else:
            h2 = int(manual_hour2.get())
        global manual_minute2
        if not manual_minute2.get().isnumeric():
            min2 = 0
        else:
            min2 = int(manual_minute2.get())
        global manual_seconds2
        if not manual_seconds2.get().isnumeric():
            s2 = 0
        else:
            s2 = int(manual_seconds2.get())
        global manual_year2
        if not manual_year2.get().isnumeric():
            y2 = 0
        else:
            y2 = int(manual_year2.get())
        global manual_month2
        if not manual_month2.get().isnumeric():
            mon2 = 0
        else:
            mon2 = int(manual_month2.get())
        global manual_day2
        if not manual_day2.get():
            d2 = 0
        else:
            d2 = int(manual_day2.get())
        event2 = f"{y2}-{mon2}-{d2} {h2}:{min2}:{s2}"
        self.manual_thread = self.Monitor.manual(event1,event2)
        self.manual_thread.start()
        self.manual_thread.join()

        # self.manual_thread = Thread(target=lambda: Monitor.manual(event1=event1, event2=event2))
        # self.manual_thread.start()
        # self.manual_thread.join()
        # self.auto_thread.join()

    def manual(self):
        self.manual_win = tk.Toplevel()
        self.manual_win.geometry("300x300")
        self.manual_win.title("scheduled")
        # auto_win.grab_set()
        a = "Enter date and time of two events : "
        msg = tk.Label(self.manual_win, text=a)
        msg.pack()
        event1 = tk.Label(self.manual_win, text="Event1 :")
        event2 = tk.Label(self.manual_win, text="Event2 :")
        event1.place(x=10, y=22)
        event2.place(x=150, y=22)
        # event1 inputs
        hour1 = tk.Label(self.manual_win, text="Hour:")
        hour1.place(x=10, y=62)
        global manual_hour1
        manual_hour1 = tk.Entry(self.manual_win, bd=1, width=5)
        manual_hour1.place(x=60, y=62)
        minute1 = tk.Label(self.manual_win, text="Minute:")
        minute1.place(x=10, y=82)
        global manual_minute1
        manual_minute1 = tk.Entry(self.manual_win, bd=1, width=5)
        manual_minute1.place(x=60, y=82)
        seconds1 = tk.Label(self.manual_win, text="Second:")
        seconds1.place(x=10, y=102)
        global manual_seconds1
        manual_seconds1 = tk.Entry(self.manual_win, bd=1, width=5)
        manual_seconds1.place(x=60, y=102)
        year1 = tk.Label(self.manual_win, text="Year:")
        year1.place(x=10, y=122)
        global manual_year1
        manual_year1 = tk.Entry(self.manual_win, bd=1, width=5)
        manual_year1.place(x=60, y=122)
        month1 = tk.Label(self.manual_win, text="Month:")
        month1.place(x=10, y=142)
        global manual_month1
        manual_month1 = tk.Entry(self.manual_win, bd=1, width=5)
        manual_month1.place(x=60, y=142)
        day1 = tk.Label(self.manual_win, text="Day:")
        day1.place(x=10, y=162)
        global manual_day1
        manual_day1 = tk.Entry(self.manual_win, bd=1, width=5)
        manual_day1.place(x=60, y=162)
        # event2 inputs
        hour2 = tk.Label(self.manual_win, text="Hour:")
        hour2.place(x=150, y=62)
        global manual_hour2
        manual_hour2 = tk.Entry(self.manual_win, bd=1, width=5)
        manual_hour2.place(x=200, y=62)
        minute2 = tk.Label(self.manual_win, text="Minute:")
        minute2.place(x=150, y=82)
        global manual_minute2
        manual_minute2 = tk.Entry(self.manual_win, bd=1, width=5)
        manual_minute2.place(x=200, y=82)
        seconds2 = tk.Label(self.manual_win, text="Second:")
        seconds2.place(x=150, y=102)
        global manual_seconds2
        manual_seconds2 = tk.Entry(self.manual_win, bd=1, width=5)
        manual_seconds2.place(x=200, y=102)
        year2 = tk.Label(self.manual_win, text="Year:")
        year2.place(x=150, y=122)
        global manual_year2
        manual_year2 = tk.Entry(self.manual_win, bd=1, width=5)
        manual_year2.place(x=200, y=122)
        month2 = tk.Label(self.manual_win, text="Month:")
        month2.place(x=150, y=142)
        global manual_month2
        manual_month2 = tk.Entry(self.manual_win, bd=1, width=5)
        manual_month2.place(x=200, y=142)
        day2 = tk.Label(self.manual_win, text="Day:")
        day2.place(x=150, y=162)
        global manual_day2
        manual_day2 = tk.Entry(self.manual_win, bd=1, width=5)
        manual_day2.place(x=200, y=162)

        button_enter = tk.Button(self.manual_win, text="ENTER",
                                 command=lambda: [self.start_manual(), self.close_sub_win()])
        button_enter.config(width=10, height=2)
        button_enter.place(x=100, y=185)

    def start_auto(self):
        global auto_hour
        if not auto_hour.get().isnumeric():
            h = 0
        else:
            h = int(auto_hour.get()) * SECONDS_IN_HOUR
        global auto_minute
        if not auto_minute.get().isnumeric():
            m = 0
        else:
            m = int(auto_minute.get()) * SECONDS_IN_MINUTE
        global auto_seconds
        if not auto_seconds.get().isnumeric():
            s = 0
        else:
            s = int(auto_seconds.get())
        self.auto_thread = Thread(target=lambda: self.Monitor.auto(h+m+s))
        self.auto_thread.start()
        # self.auto_thread.join()


    def auto(self):
        self.auto_win = tk.Tk()
        self.auto_win.geometry("280x150")
        self.auto_win.title("scheduled")
        # auto_win.grab_set()
        a = "Enter time for scheduling the services monitoring : "
        msg = tk.Label(self.auto_win, text=a)
        msg.pack()

        hour = tk.Label(self.auto_win, text="Hour:")
        hour.place(x=10, y=22)
        global auto_hour
        auto_hour = tk.Entry(self.auto_win, bd=1, width=5)
        auto_hour.place(x=60, y=22)
        minute = tk.Label(self.auto_win, text="Minute:")
        minute.place(x=10, y=42)
        global auto_minute
        auto_minute = tk.Entry(self.auto_win, bd=1, width=5)
        auto_minute.place(x=60, y=42)
        seconds = tk.Label(self.auto_win, text="Second:")
        seconds.place(x=10, y=62)
        global auto_seconds
        auto_seconds = tk.Entry(self.auto_win, bd=1, width=5)
        auto_seconds.place(x=60, y=62)
        button_enter = tk.Button(self.auto_win, text="ENTER",
                                 command=lambda: [self.start_auto(), self.close_sub_win()])
        button_enter.config(width=10, height=2)
        button_enter.place(x=30, y=100)

if __name__ == '__main__':
    GuiMonitor()
