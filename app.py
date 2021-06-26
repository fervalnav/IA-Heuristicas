import busquedas
import time
import Heuristicas
import PlanificacionAutomatica.búsqueda_espacio_estados as busqee

def busqueda(problema, objetivo):
    Heuristicas.problema=problema
    inicio=0
    fin=0
    print('Introduzca 1 para búsqueda a ciegas \nIntroduzca 2 para búsqueda con heurística')
    choose=int(input('Introduzca aqui su opción: '))
    if(choose==1):
        print('Busqueda a ciegas')
        option=int(input('Has elegido busqueda a ciegas:\n\tPara utilizar busqueda en anchura introduzca 1\n\tPara utilizar busqueda en profundidad introduzca 2'))
        if(option==1):
            print('Busqueda en anchura')
            inicio=time.time()
            result=busqee.BúsquedaEnAnchura().buscar(problema)
            fin=time.time()
        elif(option==2):
            print('Busqueda en profundidad')
            inicio=time.time()
            result=busqee.BúsquedaEnProfundidad().buscar(problema)
            fin=time.time()
        else:
             print('No has insertado opción válida')
    elif(choose==2):
        print('Has eligido búsqueda con heurística:\n\tPara utilizar el prego introduzca 1 \n\tPara utilizar delta0 introduzca 2')
        option=int(input('Introduzca aqui si opción: '))
        if(option==1):
            print('Prego')
            inicio=time.time()
            result=busquedas.busqueda_en_profundidad_H(problema.estado_inicial, objetivo, problema.acciones)
            fin=time.time()
        elif(option==2):
            print('Delta 0')
            inicio=time.time()
            result=busquedas.busqueda_en_profundidad_H_delta0(problema.estado_inicial, objetivo, problema.acciones)
            fin=time.time()
            
        else:
           print('No has insertado opción válida')
    else:
        print('No has insertado opción válida')
    
    print('-----Resultado-------')
    if(choose==1 or result=='FALLO'):
        print(result)
    else:
        [print(x.nombre) for x in result]
    tiempo=fin-inicio
    if(tiempo>0):
        print('Tiempo tardado:', tiempo)

def heuristica(problema, p):
    Heuristicas.problema=problema
    inicio=0
    fin=0
    result=0
    print('Para utilizar el prego introduzca 1 \nPara utilizar delta0 introduzca 2')
    option=int(input('Introduzca aqui si opción: '))
    if(option==1):
        print('Prego')
        inicio=time.time()
        for pred in p:
            result+=Heuristicas.prego(problema.estado_inicial,pred)
        fin=time.time()
    elif(option==2):
        print('Delta 0')
        inicio=time.time()
        for pred in p:
            result+=Heuristicas.delta0(problema.estado_inicial,pred)
        fin=time.time()
    print('Result:', result)
    tiempo=fin-inicio
    print('Tiempo tardado:', tiempo)
 