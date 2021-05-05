# import statement for tkinter
from tkinter import *

root = Tk()
root.geometry("450x300")
root.title("adding 2 numbers")

def reset():
    first_number.delete(0, END)
    second_number.delete(0, END)

def add():
    number1 = int(first_number.get())
    number2 = int(second_number.get())
    added = number1 + number2
    return answer.insert(added, added)

def exit():
    root.destroy()

first_label = Label(root, text=" Enter first Number", bd=4)
first_number = Entry(root)

second_label = Label(root, text=" Enter second Number", bd=4)
second_number = Entry(root)

third_label = Label(root, text="Your answer", bd=4)
answer = Entry(root)

number1 = Entry(root)
number2 = Entry(root)

btn1 = Button(root, text="ADD", command=add, bd=4, padx=3,)
btn2 = Button(root, text="Reset", command=reset, bd=4, padx=2,)
btn3 = Button(root, text="Exit", command=exit, bd=4, padx=3,)

first_label.place(x=0, y=0)
second_label.place(x=0, y=25)
third_label.place(x=0, y=50)
first_number.place(x=250, y=0)
second_number.place(x=250, y=25)
answer.place(x=250, y=50)
btn1.place(x=125, y=75)
btn2.place(x=175, y=75)
btn3.place(x=225, y=75)
root.mainloop()
