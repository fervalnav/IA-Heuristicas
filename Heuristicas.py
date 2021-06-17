from re import X
import PlanificacionAutomatica.problema_espacio_estados as probee
import PlanificacionAutomatica.problema_planificación_pddl as probpl


# def Heuristica(e, p):
#     if()
problema= None


def prego(e, p):
    print(e)
    print(p)
    if e.satisface_positivas(p):
        return []
    else:
        posibleAccion=[]
        for accion in problema.acciones:
            if p.items() in accion.efectosP.items():
                posibleAccion.append(accion)
        if len(posibleAccion)==0:
                print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
                return problema.acciones
        else:
            options=[]
            print(posibleAccion)
            for accion in posibleAccion:
                results=[accion]
                for pre in accion.precondicionesP:  
                    results.append(prego(pre))
                options.append(results)

            minValue=None
            minIndex=None
            for o in options:
                if(minValue is None or len(o)<minValue):
                    minValue=len(o)
                    minIndex=options.index(o)
            return options[minIndex]