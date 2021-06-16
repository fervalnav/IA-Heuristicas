import PlanificacionAutomatica.problema_planificación_pddl as probp
from tkinter import *

predicados = []
estado_inicial = probp.Estado()


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def nuevo_predicado(self):
        self.nuevo_pred = Tk()
        self.nuevo_pred.title("Nuevo predicado")
        self.label_nombre = Label(self.nuevo_pred, text="Nomenclatura predicado").grid(column=0,row=0)
        self.input_nombre = Entry(self.nuevo_pred)
        self.input_nombre.grid(column=0,row=1)

        self.label_param = Label(self.nuevo_pred, text="Parametros:").grid(column=0,row=3)
        self.input_param = Entry(self.nuevo_pred, width=50)
        self.input_param.insert(0,"a,b;c,d;...")
        self.input_param.grid(column=0,row=4, pady=5)
        self.submit = Button(self.nuevo_pred,command=self.get_predicado, text="Añadir")
        self.submit.grid(column=0, row=5)
        self.submit = Button(self.nuevo_pred,command=self.nuevo_pred.destroy, text="Aceptar")
        self.submit.grid(column=1, row=5)

        self.submit = Button(self.nuevo_pred,command=self.eliminar_ultimo_pred, text="Eliminar ultimo")
        self.submit.grid(column=2, row=5)

        for pred in predicados:
            self.label_predicados = Label(self.nuevo_pred, text= pred.name + "".join(str(e) for e in pred.dominios))
            self.label_predicados.grid(column=0,row=predicados.index(pred)+6, pady=5)
        

    def eliminar_ultimo_pred(self):
        predicados.pop()
        self.label_predicados.destroy()
        for pred in predicados:
            self.label_predicados = Label(self.nuevo_pred, text= pred.name + "".join(str(e) for e in pred.dominios))
            self.label_predicados.grid(column=0,row=predicados.index(pred)+6, pady=5)

    def get_predicado(self):
        pred = self.input_nombre.get()
        params = self.input_param.get()

        paramL = params.rsplit(";")
        p = probp.Predicado(paramL)
        p.name = pred
        if(p not in predicados):predicados.append(p)

        for pred in predicados:
            self.label_predicados = Label(self.nuevo_pred, text= pred.name + "".join(str(e) for e in pred.dominios))
            self.label_predicados.grid(column=0,row=predicados.index(pred)+6, pady=5)



    def get_estado_inicial(self):
        self.initial_Sta = self.input_iniSta.get()
        self.lista_prec = self.initial_Sta.rsplit(";")
        lista = []
        for str in self.lista_prec:
            nombre_pred = str.split("(")[0]
            literales = str.replace(")","").split("(")[1]
            estado_inicial.atomos = {}
            for atomo in estado_inicial.atomos:
                for key, value in atomo.items():
                    if key in self.atomos:
                        self.atomos[key] = self.atomos[key].union(value)
                    else:
                        self.atomos[key] = value
            print(nombre_pred + literales)


    def estado_inicial(self):
        self.initial_state = Tk()
        self.initial_state.geometry('500x300')
        self.initial_state.title("Estado inicial")
        self.label_iniSta = Label(self.initial_state, text="Precondiciones: ").grid(column=0,row=0,padx=5,pady=3)
        self.input_iniSta = Entry(self.initial_state,width=80)
        self.input_iniSta.insert(0,"en(A); hacia(abajo); sobre(D,C)")
        self.input_iniSta.grid(column=0,row=1,padx=10, pady=4)

        self.submit = Button(self.initial_state,command=self.get_estado_inicial, text="Crear estado inicial")
        self.submit.grid(column=0, row=2)

        self.label_predcDisp = Label(self.initial_state, text="Predicados disponibles: ").grid(column=0,row=3,padx=5,pady=3)
        for pred in predicados:
            self.label_predicados = Label(self.initial_state, text= pred.name + "".join(str(e) for e in pred.dominios))
            self.label_predicados.grid(column=0,row=predicados.index(pred)+4, pady=5)

    def create_widgets(self):
        self.new_pred = Button(self,command=self.nuevo_predicado, text='Nuevo predicado')
        self.initial_state = Button(self,command=self.estado_inicial, text='Estado inicial')
       
        self.new_pred.pack(side="top")
        self.initial_state.pack(side="top")

        self.label_pred = Label(self, text="Predicados")

        for str in predicados:
            self.predicados = Label(self, text=str)
            self.predicados.pack(side="right")

        self.quit = Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


    

root = Tk()
root.geometry('400x400')
app = Application(master=root)
app.mainloop()