#tonis kandmaa
#it-22
#10.01.20233

from tkinter import *


aken = Tk()
tekst = Label(aken, text="NIMI \n RÜHM: IT-22 \n 2023", font="Tahoma 16 bold italic", foreground="blue", background="black")
aken.configure(background='black')

aken.title('Tkinter "Hello World"')
aken.maxsize(800,400)
aken.resizable(0, 0)

aken.iconbitmap('favicon.ico')
logo = PhotoImage(file="m.gif").subsample(3, 3)
Label(aken, image=logo).pack(side="right")

tekst.pack()

aken.mainloop()