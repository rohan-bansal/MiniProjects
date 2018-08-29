import tkinter as tk
import time

window = tk.Tk()
window.geometry("300x300")
window.resizable(False, False)
window.title("Desktop Jitterclick Test")

score = 0
timex = 10
firstClick = False
x = 0

display = tk.Label(window, font = ("Comic Sans", 20), text = "Clicks: " + str(score))
display.place(relx = 0.5, rely = 0.2, anchor = "center")

timedisplay = tk.Label(window, font = ("Comic Sans", 12), text = str(timex))
timedisplay.place(relx = 0.1, rely = 0.05, anchor = "center")

def calcCPS():
    clickme.destroy()
    display.config(font = ("Comic Sans", 15), text = "Average Clicks Per Second:\n" + str(score / 10) + "\n\nRestart the app to\nplay again")
    display.place_forget()
    display.place(relx = 0.5, rely = 0.5, anchor = "center")

def startTimer():
    global timex, x
    timedisplay.config(text = str(timex))
    timex -= 1
    if(timex == -1):
        calcCPS()
        return
    window.after(1000, startTimer)

def increaseScore(button):
    global firstClick
    if firstClick == False:
        button.config(text = "Click")
        firstClick = True
        startTimer()
    else:
        global score
        score += 1
        display.config(text = "Clicks: " + str(score))

clickme = tk.Button(window, text = "Start", width = 6, height = 4, command = lambda: increaseScore(clickme))
clickme.place(relx = 0.5, rely = 0.5, anchor = "center")

window.mainloop()