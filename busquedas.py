import copy
from PlanificacionAutomatica.problema_planificación_pddl import AcciónPlanificación, agrupar_diccionarios
import Heuristicas


def busqueda_en_profundidad_H(e,o,acciones):
    return bep_H_rec([],[],e,o,acciones)

def bep_H_rec(plan, visitados, actual, o,acciones):
    diccs = copy.deepcopy(o)
    if actual.satisface_positivas(agrupar_diccionarios(diccs)):
        return plan
    else:
        aplicables = obtenAplicables(acciones, actual,visitados)

        ord_aplicables = ordena_heuristica(aplicables,actual,o)

        for acc in ord_aplicables:
            e = AcciónPlanificación.aplicar(acc,actual)
            plan.append(acc)
            visitados.append(e)
            res = bep_H_rec(plan,visitados, e, o,acciones)
            if res != 'FALLO':
                return res
        return 'FALLO'

def obtenAplicables(acciones, estado, visitados):
    result = []
    
    for accion in acciones:
        b = True
        if(AcciónPlanificación.es_aplicable(accion,estado)):
            new_estado = AcciónPlanificación.aplicar(accion,estado)
            for state in visitados:
                if state.atomos == new_estado.atomos:
                    b = False
            if b:
                result.append(accion)
        
    return result





def ordena_heuristica(aplicables, estado,o):
    dicc = dict()
    for accion in aplicables:
        nuevo_estado = AcciónPlanificación.aplicar(accion,estado)
        distancia = 0
        for obj in o:
            distancia += Heuristicas.prego(nuevo_estado, obj)
        dicc[accion]=distancia

    lista = list(dicc.values())
    lista.sort()
    result = []
    for valor in lista:
        for key, value in dicc.items():
            if valor == value:
                result.append(key)
    return result
    



    
