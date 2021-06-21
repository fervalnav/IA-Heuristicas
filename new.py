from re import X
import PlanificacionAutomatica.problema_espacio_estados as probee
import PlanificacionAutomatica.problema_planificación_pddl as probpl

# def Heuristica(e, p):
#     if()
problema= None
predicados = []

def incluyeEfectos(p):
    lista = []
    for accion in problema.acciones:
        for clave in p:
            if clave in accion.efectosP.keys() and p[clave]==accion.efectosP[clave]:
                lista.append(accion)
    return lista
                        

def prego(e, p):
    print('Estado incial: \n', e)
    print('Objetivo: \n', p)
    posibleAcciones = incluyeEfectos(p)
    if e.satisface_positivas(p):
        print('Satisface positivas')
        return []
    elif not e.satisface_positivas(p) and len(posibleAcciones) == 0:
        print('No hay efectos', len(problema.acciones))
        return problema.acciones
    else:

        print('Else')
        options=[]
        for accion in posibleAcciones:
            results=[]
            results.append(accion)
            for predicado in accion.precondicionesP: 
                print(predicado)
                for i in predicados:
                    if(i.name==predicado):
                        if len(i.dominios) == 0:
                            results += prego(e, i())
                        else:
                            lista = []
                            [lista.append(letra) for letra in accion.precondicionesP[predicado]]
                            if len(lista[0])==1:
                                results += prego(e, i(lista[0][0]))
                            else:
                                print(lista[0])
                                results += prego(e, i(lista[0][0]))
                        
            options.append(results)
            print(len(results))
                                
        minValue=None
        minIndex=None
        print('Longitud options: ', len(options))
        for o in options:
            print('Longitud de esta lista', len(o))
            if(minValue is None or len(o)<minValue):
                minValue=len(o)
                minIndex=options.index(o)

        return options[minIndex]