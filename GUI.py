from tkinter import *
from tkinter import messagebox
 

def añadir_campo():

    def obtener_nombre(input_nombre):
        lbl = str(input_nombre.get())
        label_nombre = Label(gui, text=lbl).grid(column=0,row=0, padx=5,pady=5)
        input_nombre = Entry(gui).grid(column=1,row=0, padx=5,pady=5)

    nuevo_campo= Tk()
    nuevo_campo.title("Nuevo parametro")
    label_nombre = Label(nuevo_campo, text="Nombre parametro").grid(column=0,row=0, padx=5,pady=5)
    input_nombre = Entry(nuevo_campo).grid(column=1,row=0, padx=5,pady=5)
    aceptar = Button(nuevo_campo, text="Añadir", command=obtener_nombre(input_nombre)).grid(column=1,row=1, padx=5,pady=5)

    



def nuevo_predicado():
    nuevo_pred = Tk()
    nuevo_pred.geometry('400x400')
    nuevo_pred.title("Nuevo predicado")
    label_nombre = Label(nuevo_pred, text="Nomenclatura predicado").grid(column=0,row=0, padx=5,pady=5)
    input_nombre = Entry(nuevo_pred, text="Hello").grid(column=1,row=0, padx=5,pady=5)
    
    nuevo_parametro = Button(nuevo_pred, text="Añadir parametro", command = añadir_campos).grid(column=1,row=1, padx=5,pady=5)


 
    

master = Tk()
master.geometry('400x400')
b1 = Button(master,command=nuevo_predicado, 
          text='Nuevo predicado').grid(row=3, 
                                    column=0, 
                                    sticky=W, 
                                    pady=4)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

master.mainloop()