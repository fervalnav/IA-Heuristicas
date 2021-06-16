from tkinter import *
from tkinter import messagebox
 



    



def nuevo_predicado():
    nuevo_pred = Tk()
    nuevo_pred.title("Nuevo predicado")
    label_nombre = Label(nuevo_pred, text="Nomenclatura predicado").grid(column=0,row=0)
    input_nombre = Entry(nuevo_pred).grid(column=0,row=1)


    label_param = Label(nuevo_pred, text="Parametros:").grid(column=0,row=3)
    input_param = Entry(nuevo_pred, width=50)
    input_param.insert(0,"{a,b};{c,d};...s")
    input_param.grid(column=0,row=4, pady=5)



    
    


 
    

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