from re import X
import PlanificacionAutomatica.problema_espacio_estados as probee
import PlanificacionAutomatica.problema_planificación_pddl as probpl

# def Heuristica(e, p):
#     if()
problema= None
predicados = []


def prego(e, p):
    print('Estado incial: \n', e)
    print('Objetivo: \n', p)
    
    if e.satisface_positivas(p):
        print('-----------------------------------')
        return []
    else:
        posibleAccion=[]
        for accion in problema.acciones:
            for clave in p:
                if clave in accion.efectosP.keys() and p[clave]==accion.efectosP[clave]: 
                        # print("Acciones: ", accion.nombre, accion.efectosP[clave])
                        # print('Objetivo: ', p)
                        posibleAccion.append(accion)
        if len(posibleAccion)==0:
            print('Aqui tambien ha entrado')
            return problema.acciones
        else:
            options=[]
            for accion in posibleAccion:
                print(accion.nombre)
                results=[accion]
                for pre in accion.precondicionesP:  
                    for i in predicados:
                        if(i.name==pre):
                            letras = []
                            for x in accion.precondicionesP[pre]:
                                for j in x:
                                    letras.append(j)
                            print(*letras) 
                            results += prego(e, i(*letras))
                options.append(results)

            minValue=None
            minIndex=None
            for o in options:
                if(minValue is None or len(o)<minValue):
                    minValue=len(o)
                    minIndex=options.index(o)

            return options[minIndex]