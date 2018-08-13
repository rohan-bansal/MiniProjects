import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.geometry("700x700")
window.title("PyPad")

class tools():
    def __init__(self):
        self.font = "Arial"
        self.fontsize = 12
        self.fontType = ""
        self.savelocation = ""

    def save(self):    
        if(self.savelocation == ""):
            self.save_as()
        else:
            t = editor.get("1.0", "end-1c")
            file_ = open(self.savelocation, "w+")
            file_.write(t)
            file_.close()

    def save_as(self):
        t = editor.get("1.0", "end-1c")
        self.savelocation = filedialog.asksaveasfilename()
        file_ = open(self.savelocation, "w+")
        file_.write(t)
        file_.close()

    def change_fonts(self, fontchange):
        self.font = fontchange
        if(self.fontType != ""):
            editor.config(font = (self.font, self.fontsize, self.fontType))
        else:
            editor.config(font = (self.font, self.fontsize))
    
    def change_fontsizeEvent(self, var, entry):
        self.fontsize = var.get()
        entry.destroy()
        if(self.fontType != ""):
            print(self.fontsize)
            editor.config(font = (self.font, self.fontsize, self.fontType))
        else:
            print(self.fontsize)
            editor.config(font = (self.font, self.fontsize))
    
    def change_fontsize(self):
        i = tk.StringVar()
        i.set("(Integer) Enter to apply")
        input_ = tk.Entry(window, textvariable = i)
        input_.bind("<Return>", lambda event, var = i, entry = input_: self.change_fontsizeEvent(var, entry))
        input_.place(x = 0, y = 0)
        

    def change_fontType(self, type_):
        self.fontType = type_
        if(self.fontType != ""):
            editor.config(font = (self.font, self.fontsize, self.fontType))
        else:
            editor.config(font = (self.font, self.fontsize))


utils = tools()

global editor
editor = tk.Text(window, height = 700, width = 99)
editor.grid()

MenuBar = tk.Menu(window)
FileMenu = tk.Menu(MenuBar, tearoff = 0)
Style = tk.Menu(MenuBar, tearoff = 0)
Font = tk.Menu(MenuBar, tearoff = 0)
FontType = tk.Menu(MenuBar, tearoff = 0)

FileMenu.add_command(label = "Save", command = utils.save)
FileMenu.add_command(label = "Save As", command = utils.save_as)


Font.add_command(label = "Helvetica", command = lambda: utils.change_fonts("Helvetica"))
Font.add_command(label = "Comic Sans", command = lambda: utils.change_fonts("Comic Sans"))
Font.add_command(label = "Arial", command = lambda: utils.change_fonts("Arial"))
Font.add_command(label = "Times", command = lambda: utils.change_fonts("Times"))
Font.add_command(label = "Courier", command = lambda: utils.change_fonts("Courier"))
Font.add_command(label = "Verdana", command = lambda: utils.change_fonts("Verdana"))

FontType.add_command(label = "Bold", command = lambda: utils.change_fontType("bold"))
FontType.add_command(label = "Italic", command = lambda: utils.change_fontType("italic"))

Style.add_cascade(label = "Font", menu = Font)
Style.add_cascade(label = "Font Options", menu = FontType)
Style.add_command(label = "Font Size", command = utils.change_fontsize)

MenuBar.add_cascade(label="File", menu = FileMenu)
MenuBar.add_cascade(label="Styling", menu = Style)

window.config(menu = MenuBar)

window.mainloop()