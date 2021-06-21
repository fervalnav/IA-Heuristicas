from re import X
import PlanificacionAutomatica.problema_espacio_estados as probee
import PlanificacionAutomatica.problema_planificación_pddl as probpl
import auxiliares
problema= None
ultimo_estado = None  
accionesUsadas  =[]

def generar_estado(predicado):
    return probpl.Estado(predicado)


def prego(e, p):
    # print('Estado incial: \n', e)
    print('Objetivo: \n', p)
    # ultimo_estado = probpl.Estado( p )
    posibleAcciones = auxiliares.incluyeEfectos(p, problema.acciones)
    [print(x.nombre) for x in posibleAcciones]
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
                print(predicado)
                print(accion.precondicionesP[predicado])
                pred = auxiliares.get_predicado(predicado, accion.precondicionesP[predicado])
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
