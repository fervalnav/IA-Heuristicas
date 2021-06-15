from tkinter import *
from tkinter import messagebox
 
 
class GUI(Frame):
 
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.createWidgets()
 
    def deleteLastCharacter(self):
        textLength = len(self.display.get())
 
        if textLength >= 1:
            self.display.delete(textLength - 1, END)
        if textLength == 1:
            self.replaceText("0")
 
    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)
 
    def append(self, text):
        actualText = self.display.get()
        textLength = len(actualText)
        if actualText == "0":
            self.replaceText(text)
        else:
            self.display.insert(textLength, text)
 
    def evaluate(self):
        try:
            self.replaceText(eval(self.display.get()))
        except (SyntaxError, AttributeError):
            messagebox.showerror("Error", "Syntax Error")
            self.replaceText("0")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot Divide by 0")
            self.replaceText("0")
 
    def containsSigns(self):
        operatorList = ["*", "/", "+", "-"]
        display = self.display.get()
        for c in display:
            if c in operatorList:
                 return True
        return False
 
    def changeSign(self):
        if self.containsSigns():
            self.evaluate()
        firstChar = self.display.get()[0]
        if firstChar == "0":
            pass
        elif firstChar == "-":
            self.display.delete(0)
        else:
            self.display.insert(0, "-")
 
    def inverse(self):
        self.display.insert(0, "1/(")
        self.append(")")
        self.evaluate()
 
    def createWidgets(self):
        self.display = Entry(self, font=("Arial", 24), relief=RAISED, justify=RIGHT, bg='darkblue', fg='red', borderwidth=0)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")
 
        
 
 
gui = Tk()
gui.title("Heuristica")
gui.resizable(False, False)
gui.config(cursor="pencil")
root = GUI(gui).grid()
gui.mainloop()