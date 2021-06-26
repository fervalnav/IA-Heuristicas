from re import X
import auxiliares


problema= None

def delta0(e,p):
    accionesUsadas = []
    return delta0_rec(e,p,accionesUsadas)
def delta0_rec(e, p, accionesUsadas):
    posiblesAcciones=auxiliares.incluyeEfectos(p, problema.acciones,accionesUsadas)
    if e.satisface_positivas(p):
        return 0
    elif len(posiblesAcciones)==0:
        return float('Inf')
    else:
        result= None
        for accion in posiblesAcciones:
            option=1
            accionesUsadas.append(accion)
            for q in accion.precondicionesP:
                pred=auxiliares.get_predicado(q, accion.precondicionesP[q])
                option+=delta0_rec(e, pred)
            if result==None or option<result:
                result=option
        return result


def prego(e,p):
    accionesUsadas = []
    return len(pregoRec(e, p, accionesUsadas))

def pregoRec(e, p, accionesUsadas):
    accionesPosibles = auxiliares.incluyeEfectos(p, problema.acciones, accionesUsadas)
    if e.satisface_positivas(p):
        return []
    elif len(accionesPosibles)==0:
        return problema.acciones
    else:
        opciones = []
        for accion in accionesPosibles:
            
            result =[accion]
            accionesUsadas.append(accion)
            for pred in accion.precondicionesP:  
                newP = auxiliares.get_predicado(pred, accion.precondicionesP[pred])
                result += pregoRec(e,newP, accionesUsadas)
            opciones.append(result)
    
        minValue = None
        opcion = None
        for o in opciones:
            if minValue is None or len(o)<minValue:
                minValue = len(o)
                opcion = o
        return opcion