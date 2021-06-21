from re import X
import PlanificacionAutomatica.problema_espacio_estados as probee
import PlanificacionAutomatica.problema_planificación_pddl as probpl

# def Heuristica(e, p):
#     if()
problema= None
predicados = []
ultimo_estado = None  
accionesUsadas  =[]

def get_predicado(name, listaArg):
    for predicado in predicados:
        if predicado.name==name: 
            if len(predicado.dominios) == 0:
                return predicado()
            else:
                lista = []
                [lista.append(letra) for letra in listaArg]
                if len(lista[0])==1:
                    return predicado(lista[0][0])
                else:
                    return predicado(*lista[0])


def generar_estado(predicado):
    return probpl.Estado(predicado)



def incluyeEfectos(p):
    lista = []
    for accion in problema.acciones:
        for clave in p:
            if clave in accion.efectosP.keys() and p[clave]==accion.efectosP[clave]:
                lista.append(accion)
    return lista


def prego(e, p):
    # print('Estado incial: \n', e)
    print('Objetivo: \n', p)
    # ultimo_estado = probpl.Estado( p )
    posibleAcciones = incluyeEfectos(p)
    if e.satisface_positivas(p):
        print('Satisface positivas')
        return []
    elif not e.satisface_positivas(p) and len(posibleAcciones):
        print('No hay efectos', len(problema.acciones))
        return problema.acciones
    else:

        print('Else')
        options=[]
        for accion in posibleAcciones:
            print('Accion: ', accion.nombre, 'Precondiciones: ', accion.precondicionesP, 'Efectos: ', accion.efectosP)
            results=[]
            results.append(accion)
            for predicado in accion.precondicionesP: 
                print(predicado)
                print(accion.precondicionesP[predicado])
                pred = get_predicado(predicado, accion.precondicionesP[predicado])
                results += prego(e, pred)
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
