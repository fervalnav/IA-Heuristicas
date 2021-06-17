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
        return []
    else:
        posibleAccion=[]
        for accion in problema.acciones:
            for clave in p:
                if clave in accion.efectosP.keys() and p[clave]==accion.efectosP[clave]: 
                        print("Acciones: ", accion.efectosP[clave])
                        print('Objetivo: ', p[clave])
                        posibleAccion.append(accion)
        if len(posibleAccion)==0:
                return problema.acciones
        else:
            options=[]
            for accion in posibleAccion:
                results=[accion]
                print(accion.precondicionesP)
                for pre in accion.precondicionesP:  
                    for i in predicados:
                        if(i.name==pre):
                            print('Aqui')
                            letras = []
                            for x in accion.precondicionesP[pre]:
                                for j in x:
                                    letras.append("'" + j + "'")
                            print(letras)
                            results.append(prego(e, i(*letras)))
                options.append(results)

            minValue=None
            minIndex=None
            for o in options:
                if(minValue is None or len(o)<minValue):
                    minValue=len(o)
                    minIndex=options.index(o)
            return options[minIndex]