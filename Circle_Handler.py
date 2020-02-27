"""
Cyrkiel Handler v.0.1
Cracow, February 2020

Circle Area Functions by Maciej Kusy
GUI by Adam Goździelewski
"""

from tkinter import *

# DEFINING CIRCLE AREA FUNCTIONS

def circle_area(x):
    pi = 3.141592
    area = pi * (float(x)*float(x))
    write("The area of a wheel with a radius of " + x + "cm is " + (str(round(float(area),4)) + "cm2.\n\n"))

def calculate():
    r = entry_box.get()
    if r.isalpha() or r == "":
        write("Sorry, incorrect input, try again.\n\n")
    circle_area(r)

# GUI SETUP

root = Tk()
root.geometry("640x420")
root.title("Cyrkiel Handler by Collabo Tests")

# GUI ELEMENTS SETUP

left = Frame(root, borderwidth=2, relief="solid")
right = Frame(root, borderwidth=2, relief="solid")
left_con = Frame(left, borderwidth=2, relief="solid")
right_con = Frame(right, borderwidth=2, relief="solid")

plotno = Canvas(left_con, width=100, height=100)
Canvas.create_oval(plotno, 100, 100, 40, 40)
Canvas.create_arc(plotno, 100, 100, 40, 40)
Canvas.create_text(plotno, 84, 62, text="r")

title = Label(left_con, text="Cyrkiel Handler", fg="black", font=("Verdana", 24))
undertitle = Label(left_con, text="by Collabo Tests", fg="black", font=("Verdana", 10))

message_box = Text(left_con, width=48, height=12, wrap=WORD, fg="black", font=("Courier New", 10))
message_box.config(state=DISABLED)
entry_box = Entry(right_con)

button_calc = Button(right_con, text="Calculate", background="gray", fg="white", font=("Courier New", 12, "bold"), command=lambda: calculate())

# DEFINING WRITE FUNCTION

def write(string):
    message_box.config(state=NORMAL)
    message_box.insert("end", string)
    message_box.see("end")
    message_box.config(state=DISABLED)

# LAYOUT SETUP

left.pack(side="left", expand=True, fill="both")
right.pack(side="right", expand=True, fill="both")
left_con.pack(expand=True, fill="both", padx=10, pady=10)
right_con.pack(expand=True, fill="both", padx=10, pady=10)

title.pack(padx=10, pady=10)
undertitle.pack()
plotno.pack(padx=10, pady=5)
message_box.pack(padx=10, pady=5)

entry_box.grid(column=0, row=0, padx=10, pady=10)
button_calc.grid(column=0, row=1, padx=10, pady=10)

# USER INSTRUCTIONS

write("Please provide value for circle radius (r) and click 'Calculate' to get the circle's area.\n\n")

# COMMENCING LOOP

root.mainloop()
