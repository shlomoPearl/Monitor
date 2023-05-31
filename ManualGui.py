import tkinter as tk

global manual_hour1
global manual_hour2
global manual_minute1
global manual_minute2
global manual_second1
global manual_second2
global manual_year1
global manual_year2
global manual_month1
global manual_month2
global manual_day1
global manual_day2


class ManualGui:
    def __init__(self):
        self.manual_win = tk.Tk()
        self.event = None

    def close_sub_win(self):
        self.manual_win.destroy()

    def start_manual(self):
        # event1 inputs
        global manual_hour1
        if not manual_hour1.get().isnumeric():
            h1 = 0
        else:
            h1 = int(manual_hour1.get())
        global manual_minute1
        if not manual_minute1.get().isnumeric():
            min1 = 0
        else:
            min1 = int(manual_minute1.get())
        global manual_second1
        if not manual_second1.get().isnumeric():
            s1 = 0
        else:
            s1 = int(manual_second1.get())
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
        global manual_second2
        if not manual_second2.get().isnumeric():
            s2 = 0
        else:
            s2 = int(manual_second2.get())
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
        self.event = event1, event2

    def manual(self):
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
        second1 = tk.Label(self.manual_win, text="Second:")
        second1.place(x=10, y=102)
        global manual_second1
        manual_second1 = tk.Entry(self.manual_win, bd=1, width=5)
        manual_second1.place(x=60, y=102)
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
        seconds = tk.Label(self.manual_win, text="Second:")
        seconds.place(x=150, y=102)
        global manual_second2
        manual_second2 = tk.Entry(self.manual_win, bd=1, width=5)
        manual_second2.place(x=200, y=102)
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
        self.manual_win.mainloop()
