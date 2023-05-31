import tkinter as tk
import Monitor
SECONDS_IN_HOUR = 60 * 60
SECONDS_IN_MINUTE = 60
global auto_hour
global auto_minute
global auto_seconds


class AutoGui:
    def __init__(self):
        self.t = None
        self.auto_win = tk.Tk()

    def close_sub_win(self):
        self.auto_win.destroy()

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
        self.t = h + m + s
        # self.auto_monitor.auto()

    def auto(self):
        # self.auto_win = tk.Tk()
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
        self.auto_win.mainloop()
