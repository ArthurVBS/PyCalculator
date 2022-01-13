import os, re
from tkinter import *

directory = os.path.dirname(__file__)

window = Tk()

bg = "#fafafa"
fg = "#000"
width = 335
height = 360
width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()
pos_x = int(width_screen / 2 - width / 2)
pos_y = int(height_screen / 2 - height / 2)

window.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
window.title("Calculator")
window.iconbitmap(directory + "./icon.ico")
window.resizable(False,False)
window.configure(background = bg)

#functions

def delete():
    c = len(entry_01.get()) - 1
    entry_01.delete(c,END)

def click_btn(n):
    entry_01.insert(END, n)

def equal():
    equations = entry_01.get()
    equations = re.sub(r"[^\d\.\/\*\-\+\^e\(\)]",r"",equations, 0)
    equations = re.sub(r"([\.\+\/\-\*])\1", r"\1", equations, 0)
    equations = re.sub(r"\*?\(\)", "", equations)

    try:
        result = eval(equations)
        lbl_01.config(text=f"{equations} = {result}")
        entry_01.delete(0,END)
        entry_01.insert(END, result)

    except OverflowError:
        lbl_01.config(text="Sorry, too big result")
    except Exception:
        lbl_01.config(text="Invalid equation")

#Label

lbl_01 = Label(window, text= "Waiting for a math account...", anchor=E, justify="right", bg=bg)
lbl_01.place(x=10, y=10, width=315, height=20)

#Entry

entry_01 = Entry(window, font = "times 28 normal", justify="right", bd=1, relief="flat", bg="#f1f1f1",
                highlightthickness=1, highlightcolor="#ccc")
entry_01.place(x=10, y=40, width=315, height=50)

#Numeric Buttons

btn_9 = Button(window, text = "9", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: click_btn("9"))
btn_9.place(x=140, y=100, width=55, height=55)

btn_8 = Button(window, text = "8", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: click_btn("8"))
btn_8.place(x=75, y=100, width=55, height=55)

btn_7 = Button(window, text = "7", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: click_btn("7"))
btn_7.place(x=10, y=100, width=55, height=55)

btn_6 = Button(window, text = "6", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: click_btn("6"))
btn_6.place(x=140, y=165, width=55, height=55)

btn_5 = Button(window, text = "5", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: click_btn("5"))
btn_5.place(x=75, y=165, width=55, height=55)

btn_4 = Button(window, text = "4", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: click_btn("4"))
btn_4.place(x=10, y=165, width=55, height=55)

btn_3 = Button(window, text = "3", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: click_btn("3"))
btn_3.place(x=140, y=230, width=55, height=55)

btn_2 = Button(window, text = "2", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: click_btn("2"))
btn_2.place(x=75, y=230, width=55, height=55)

btn_1 = Button(window, text = "1", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: click_btn("1"))
btn_1.place(x=10, y=230, width=55, height=55)

btn_0 = Button(window, text = "0", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2",
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                anchor=W, padx=20, command= lambda: click_btn("0"))
btn_0.place(x=10, y=295, width=120, height=55)

#Math operations Buttons

btn_addition = Button(window, text = "+", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: click_btn("+"))
btn_addition.place(x=205, y=100, width=55, height=55)

btn_subtraction = Button(window, text = "-", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: click_btn("-"))
btn_subtraction.place(x=205, y=165, width=55, height=55)

btn_multiplication = Button(window, text = "*", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: click_btn("*"))
btn_multiplication.place(x=205, y=230, width=55, height=55)

btn_division = Button(window, text = "/", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: click_btn("/"))
btn_division.place(x=205, y=295, width=55, height=55)

#Other Buttons

btn_dot = Button(window, text = ".", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: click_btn("."))
btn_dot.place(x=140, y=295, width=55, height=55)

btn_delete = Button(window, text = "C", font = "times 20 normal", bg = "#e44", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: delete())
btn_delete.place(x=270, y=100, width=55, height=55)

btn_open_parenthesis = Button(window, text = "(", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: click_btn("("))
btn_open_parenthesis.place(x=270, y=165, width=55, height=55)

btn_close_parenthesis = Button(window, text = ")", font = "times 20 normal", bg = "#eee", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: click_btn(")"))
btn_close_parenthesis.place(x=270, y=230, width=55, height=55)

btn_equal = Button(window, text = "=", font = "times 20 normal", bg = "#5ae", bd = 1, relief = "solid", cursor="hand2", 
                highlightthickness=0, highlightcolor="#ccc", activebackground="#ccc", highlightbackground="#ccc",
                command= lambda: equal())
btn_equal.place(x=270, y=295, width=55, height=55)

window.mainloop()
