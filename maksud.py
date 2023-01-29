def arvuta():
    hind = sisestus.get()
    km = var.get()
    vastus = float(hind)*float(km)/100
    print(vastus)


from tkinter import *

#akna seaded
aken = Tk()
aken.title('MAKSUD')

#sildid
silt = Label(aken, text="Hind kmita:")
silt.grid(row=0,column=0)

silt = Label(aken, text="Hind kmita:")
silt.grid(row=1,column=0)
silt = Label(aken, text="_________________________________________________________")
silt.grid(row=3,column=0,columnspan=2)
silt = Label(aken, text="kaibemaks:")
silt.grid(row=4,column=0)
silt = Label(aken, text="Hind kmiga:")
silt.grid(row=5,column=0)

valjund = Label(aken, text="{km} eurot")
valjund.grid(row=4,column=1)
valjund2 = Label(aken, text="{vastus} eurot")
valjund2.grid(row=5,column=1)

#sisestusväljad
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)

#nupud
nupp1 = Button(aken, text="Arvuta", width=10, command=arvuta)
nupp1.grid(row=6, column=1)


#
var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=9)
valikukast.grid(row=1, column=1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=20)
valikukast.grid(row=2, column=1)



#ee

if valikukast==20:
    Maksud = sisestus*0,2
    print(Maksud)
    
    

aken.mainloop()
