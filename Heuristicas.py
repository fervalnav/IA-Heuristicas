from re import X
import PlanificacionAutomatica.problema_espacio_estados as probee
import PlanificacionAutomatica.problema_planificación_pddl as probpl


# def Heuristica(e, p):
#     if()
esquemas=[]


def prego(e, p):
    print(e)
    print(p)

    if e.satisface_positivas(p):
        return []
    else:
        result=[]
        for esquema in esquemas:
            acciones=esquema.obtener_acciones()
            for a in acciones:
                if p not in a.efectosP:
                    result.append(a)

        # accionesP=[]
        # for a in acciones:
        #     for x in a.obtener_acciones():
        #         for key in p:
        #             if key in x.efectosP.keys():
        #                 print('a')
        #                 print(p)
        #                 print(x.efectosP)
        #                 if p[key] in x.efectosP[key]:
        #                     print('b')
        #                     accionesP.append(x.nombre)
        if len(result)==0:
            print('He entrado en len=0')
            return esquemas
        else:
            options=[]
            for a in result:
                option=[a]
                for pre in a.precondicionesP:
                    option.append(prego(e, pre))
                options.append(option)
            minValue=None
            minIndex=None
            for o in options:
                if(minValue is None or len(o)<minValue):
                    minValue=len(o)
                    minIndex=options.index(o)
            return options[minIndex]