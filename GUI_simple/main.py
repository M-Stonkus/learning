import tkinter


def bclick():
    calculate = round(float(input.get())/1.609,3)
    mvalue.config(text=str(calculate))

window = tkinter.Tk()

window.title("GUI")
window.minsize(400, 250)
window.config(padx=40, pady=40)

km = tkinter.Label(text="Km", font=("Arial", 14, "normal"))
km.grid(column=2, row=0)
km.config(padx=20, pady=20)

eq = tkinter.Label(text="is equal to", font=("Arial", 14, "normal"))
eq.grid(column=0, row=1)
eq.config(padx=20, pady=20)

mvalue = tkinter.Label(text="0", font=("Arial", 14, "normal"))
mvalue.grid(column=1, row=1)
mvalue.config(padx=20, pady=20)

miles = tkinter.Label(text="Miles", font=("Arial", 14, "normal"))
miles.grid(column=2, row=1)
miles.config(padx=20, pady=20)

button1 =tkinter.Button(text="CALCULATE", command=bclick, font=("Arial", 14, "normal"))
button1.grid(column=1, row=2)
button1.config(padx=20, pady=20)

input = tkinter.Entry(font=("Arial", 14, "normal"))
input.insert(1, string = "0")
input.grid(column=1, row=0)








window.mainloop()
