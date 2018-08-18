import tkinter as tk
from tkinter import messagebox
import time, sys, os
import datetime

window = tk.Tk()
window.geometry("400x300")
window.resizable(False, False)
window.title("Stopwatch")

try:
    import pygame
except ImportError:
    if messagebox.askyesno('ImportFix', 'There is a missing dependency needed for the program to work\
    (module "pygame", for sound). Would you like the program to install it?') == True:    
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip3', 'install', '--user', 'pygame'])
        import pygame
    else:
        sys.exit()

class Watch():
    def __init__(self, root, label):
        self.root = root
        self.timelabel = label
        self.hours = 0
        self.milliseconds = 0
        self.seconds = 0
        self.minutes = 0
        self.stoptheclock = 0
        self.timecheck = ""

    def start_stopwatch(self):
        self.stoptheclock = 0
        while(True):
            if(self.stoptheclock == 1):
                break
            self.milliseconds += 1
            if(self.milliseconds == 100):
                self.seconds += 1
                self.milliseconds = 0
            if(self.seconds == 60):
                self.minutes += 1
                self.seconds = 0   
            self.timelabel.config(text = str(self.minutes) + " : " + str(self.seconds) + " : " + str(self.milliseconds))
            time.sleep(0.005)
            self.root.update()

    def stop_clock(self, exists=False, timer=None):
        if(exists == True):
            if(timer.cget("text") == "Resume"):
                timer.config(text = "Pause")
                self.startTimer()
                return
            timer.config(text = "Resume")
            self.stoptheclock = 1
        else:
            self.stoptheclock = 1

    def reset_clock(self):
        self.milliseconds = 0
        self.seconds = 0
        self.minutes = 0            
        self.timelabel.config(text = str(self.minutes) + " : " + str(self.seconds) + " : " + str(self.milliseconds))
        self.root.update()

    def TimerSet(self):
        self.hours = int(h.get())
        self.minutes = int(m.get())
        self.seconds = int(s.get())
        self.startTimer()

    def startTimer(self):
        self.stoptheclock = 0
        while(True):
            if(self.stoptheclock == 1):
                break
            if(self.seconds != 0):
                self.seconds -= 1
            else:
                if(self.minutes != 0):
                    self.seconds = 59
                    self.minutes -= 1
                else:
                    if(self.hours != 0):
                        self.minutes = 59
                        self.seconds = 59
                        self.hours -= 1
                    else:
                        break
            self.timelabel.config(text = str(self.hours) + " : " + str(self.minutes) + " : " + str(self.seconds))
            self.root.update()
            time.sleep(1)
        if(self.stoptheclock == 1):
            pass
        else:
            self.timelabel.config(text = " TIMER FINISHED ", font=("Comic Sans", 24))
            path = os.path.dirname(os.path.abspath(__file__))
            pygame.mixer.init()
            pygame.mixer.music.load(path + "/Beep/alarm.mp3")
            pygame.mixer.music.play()

    def setAlarm(self, timex = ""):
        if(timex != ""):
            self.timecheck = timex
        else:
            self.hours = h.get()
            self.minutes = m.get()
            y = [self.hours, self.minutes, self.timecheck]
            if y[2] == "pm" and y[0] != "12":
                y[0] = str(12 + int(y[0]))
            if len(y[1]) != 2:
                y[1] = "0" + y[1]
            self.timelabel.config(text = self.hours + " : " + y[1] + " " + y[2])
            self.stoptheclock = 0
            while(True):
                if(self.stoptheclock == 1):
                    break
                time.sleep(0.01)
                rn = str(datetime.datetime.now().time())
                if(rn >= (y[0] + ":" + y[1] + ":00.000000")):
                    break
                self.root.update()
            if(self.stoptheclock == 1):
                pass
            else:
                self.timelabel.config(text = " ALARM RINGING ", font=("Comic Sans", 24))
                path = os.path.dirname(os.path.abspath(__file__))
                pygame.mixer.init()
                pygame.mixer.music.load(path + "/Beep/alarm.mp3")
                pygame.mixer.music.play()

def StopwatchB1():
    display = tk.Label(window, text = "0 : 0 : 0", font=("Comic Sans", 44))
    display.place(relx = 0.5, rely = 0.4, anchor = "center")
    stopwatch = Watch(window, display)

    pause = tk.Button(window, text = "PAUSE", width = 10, height = 1, command = stopwatch.stop_clock)
    pause.place(x = 140, y = 200)
    start = tk.Button(window, text = "START", width = 10, height = 1, command = stopwatch.start_stopwatch)
    start.place(x = 140,y = 230)
    reset = tk.Button(window, text = "RESET", width = 10, height = 1, command = stopwatch.reset_clock)
    reset.place(x = 140, y = 260)

def TimerB1():
    global h, m, s, display
    display = tk.Label(window, text = "0 : 0 : 0", font=("Comic Sans", 44))
    display.place(relx = 0.5, rely = 0.4, anchor = "center")

    timer = Watch(window, display)
    h = tk.StringVar()
    m = tk.StringVar()
    s = tk.StringVar()

    hours = tk.Spinbox(window, from_ = 0, to = 24, width = 7, textvariable = h)
    minutes = tk.Spinbox(window, from_ = 0, to = 59, width = 7, textvariable = m)
    seconds = tk.Spinbox(window, from_ = 0, to = 59, width = 7, textvariable = s)
    pause = tk.Button(window, text = "Pause", command = lambda: timer.stop_clock(True, pause))
    h.set("Hours")
    m.set("Minutes")
    s.set("Seconds")
    hours.place(relx = 0.5, rely = 0.6, anchor = "center")
    minutes.place(relx = 0.5, rely = 0.7, anchor = "center")
    seconds.place(relx = 0.5, rely = 0.8, anchor = "center")
    ok = tk.Button(window, text = "Set", command = timer.TimerSet)
    ok.place(relx = 0.5, rely = 0.9, anchor = "center")
    pause.place(relx = 0.6, rely = 0.6)

def AlarmB1():
    global h, m, display
    display = tk.Label(window, text = "[Alarm]\n00 : 00 : 00", font = ("Comic Sans", 24))
    display.place(relx = 0.5, rely = 0.4, anchor = "center")

    alarm = Watch(window, display)
    h = tk.StringVar()
    m = tk.StringVar()
    hours = tk.Spinbox(window, from_ = 0, to = 12, width = 7, textvariable = h)
    minutes = tk.Spinbox(window, from_ = 0, to = 59, width = 7, textvariable = m)
    setAM = tk.Button(window, text = "AM", command = lambda: alarm.setAlarm("am"))
    setPM = tk.Button(window, text = "PM", command = lambda: alarm.setAlarm("pm"))
    canc = tk.Button(window, text = "Cancel", command = alarm.stop_clock)
    h.set("Hour")
    m.set("Minute")
    hours.place(relx = 0.5, rely = 0.6, anchor = "center")
    minutes.place(relx = 0.5, rely = 0.7, anchor = "center")
    setAM.place(relx = 0.7, rely = 0.55)
    setPM.place(relx = 0.7, rely = 0.65)
    ok = tk.Button(window, text = "Set", command = alarm.setAlarm)
    ok.place(relx = 0.5, rely = 0.9, anchor = "center")
    canc.place(relx = 0.7, rely = 0.8)

def reRoute(path):
    for widget in window.winfo_children():
        widget.destroy()
    create_toplevel()
    if(path == "alarm"):
        AlarmB1()
    elif(path == "timer"):
        TimerB1()
    elif(path == "stopwatch"):
        StopwatchB1()

def create_toplevel():
    choose = tk.Toplevel(window)
    choose.resizable(False, False)

    StopwatchB = tk.Button(choose, text = "Stopwatch", command = lambda: reRoute("stopwatch"))
    TimerB = tk.Button(choose, text = "Timer", command = lambda: reRoute("timer"))
    AlarmB = tk.Button(choose, text = "Alarm", command = lambda: reRoute("alarm"))

    TimerB.pack(padx = 20, pady = 5)
    StopwatchB.pack(padx = 20, pady = 5)
    AlarmB.pack(padx = 20, pady = 5)

create_toplevel()
window.mainloop()
