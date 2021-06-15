import PlanificacionAutomatica.problema_espacio_estados as probee


# def Heuristica(e, p):
#     if()
acciones=[]

def prego(e, p):
    if e.satisface_positivas(p):
        return []
    else:
        accionesP=[]
        for a in acciones:
            if p in a.efectosP:
                accionesP.append(a)
        if accionesP.count()==0:
            return acciones
        else:
            options=[]
            for a in accionesP:
                option=[a]
                for pre in a.precondicionesP:
                    option.append(prego(e, pre))
                options.append(option)
            maxValue=None
            maxIndex=None
            for o in options:
                if(maxValue is None or o.count()>maxValue):
                    maxValue=o.count()
                    maxIndex=options.index(o)
            return options[maxIndex]