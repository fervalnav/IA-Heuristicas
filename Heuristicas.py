from re import X
import PlanificacionAutomatica.problema_espacio_estados as probee
import PlanificacionAutomatica.problema_planificación_pddl as probpl
import auxiliares


problema= None

def heuristica(e, p):
    posiblesAcciones=auxiliares.incluyeEfectos(p, problema.acciones)
    if e.satisface_positivas(p):
        return 0
    elif len(posiblesAcciones)==0:
        return 9999999999999
    else:
        result= None
        for accion in posiblesAcciones:
            option=1
            for q in accion.precondicionesP:
                pred=auxiliares.get_predicado(q, accion.precondicionesP[q])
                option+=heuristica(e, pred)
            if result==None or option<result:
                result=option
        return result