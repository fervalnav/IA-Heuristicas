from re import X
import PlanificacionAutomatica.problema_espacio_estados as probee
import PlanificacionAutomatica.problema_planificación_pddl as probpl
import auxiliares
problema= None
accionesUsadas  =[]

def generar_estado(predicado):
    return probpl.Estado(predicado)


def prego(e, p):
    print('Objetivo: \n', p)
    posibleAcciones = auxiliares.incluyeEfectos(p, problema.acciones)
    # [print(x.nombre) for x in posibleAcciones]
    if e.satisface_positivas(p):
        print('Satisface positivas')
        return []
    elif not e.satisface_positivas(p) and len(posibleAcciones)==0:  # 0=false, 1=true
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
                # print(accion.precondicionesP[predicado])
                pred = auxiliares.get_predicado(predicado, accion.precondicionesP[predicado])
                results += prego(e, pred)
                break
                
            options.append(results)
                                
        minValue=None
        minIndex=None
        print('Longitud options: ', len(options))
        for o in options:
            print('Listas: ',[a.nombre for a in o])
            if(minValue is None or len(o)<minValue):
                minValue=len(o)
                minIndex=options.index(o)
            print(minValue, len(o), minIndex)

        return options[minIndex]


def nuevoIntento(e, p):
    accionesPosibles = auxiliares.incluyeEfectos(p, problema.acciones)
    if e.satisface_positivas(p):
        return []
    elif len(accionesPosibles)==0:
        return problema.acciones
    else:
        opciones = []
        for accion in accionesPosibles:
            
            result =[accion]
            
            for pred in accion.precondicionesP:  
                newP = auxiliares.get_predicado(pred, accion.precondicionesP[pred])
                result += nuevoIntento(e,newP)
            opciones.append(result)
            
    
        minValue = None
        opcion = None
        
        [print(len(o)) for o in opciones]
        for o in opciones:
            if minValue is None or len(o)<minValue:
                minValue = len(o)
                opcion = o
        return opcion


























