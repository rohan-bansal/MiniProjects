import tkinter as tk
import time

window = tk.Tk()
window.geometry("400x300")
window.resizable(False, False)
window.title("Stopwatch")

class Watch():
    def __init__(self, root, label):
        self.root = root
        self.timelabel = label
        self.milliseconds = 0
        self.seconds = 0
        self.minutes = 0
        self.stoptheclock = 0

    def start_watch(self):
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
            time.sleep(0.01)
            self.root.update()

    def stop_watch(self):
        self.stoptheclock = 1

    def reset_clock(self):
        self.milliseconds = 0
        self.seconds = 0
        self.minutes = 0            
        self.timelabel.config(text = str(self.minutes) + " : " + str(self.seconds) + " : " + str(self.milliseconds))
        self.root.update()


display = tk.Label(window, text = "0 : 0 : 0", font=("Comic Sans", 44))
display.place(relx = 0.5, rely = 0.4, anchor = "center")

stopwatch = Watch(window, display)

pause = tk.Button(window, text = "PAUSE", width = 10, height = 1, command = stopwatch.stop_watch)
pause.place(x = 140, y = 200)

start = tk.Button(window, text = "START", width = 10, height = 1, command = stopwatch.start_watch)
start.place(x = 140,y = 230)

reset = tk.Button(window, text = "RESET", width = 10, height = 1, command = stopwatch.reset_clock)
reset.place(x = 140, y = 260)

window.mainloop()