import busquedas
import time
import Heuristicas
import PlanificacionAutomatica.búsqueda_espacio_estados as busqee



def busqueda(problema, objetivo):
    Heuristicas.problema=problema
    inicio=0
    fin=0
    result = []
    print('Introduzca 1 para búsqueda a ciegas \nIntroduzca 2 para búsqueda con heurística')
    choose=int(input('\tIntroduzca aqui su opción: '))
    if(choose==1):
        print('\nHa elegido busqueda a ciegas:\nPara utilizar busqueda en anchura introduzca 1\nPara utilizar busqueda en profundidad introduzca 2')
        option=int(input('\tIntroduzca aqui su opción: '))
        if(option==1):
            print('Busqueda en anchura')
            inicio=time.time()
            res = busqee.BúsquedaEnAnchura()
            result=res.buscar(problema)
            fin=time.time()
        elif(option==2):
            print('Busqueda en profundidad')
            inicio=time.time()
            res = busqee.BúsquedaEnAnchura()
            result=res.buscar(problema)
            fin=time.time()
        else:
             print('No has insertado opción válida')
    elif(choose==2):
        print('\nHa eligido búsqueda con heurística:\nPara utilizar el prego introduzca 1 \nPara utilizar delta0 introduzca 2')
        option=int(input('\tIntroduzca aqui si opción: '))
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
           print('No ha insertado opción válida')
    else:
        print('No ha insertado opción válida')
    
    print('\n-----Resultado-------')
    if(choose==1 or result=='FALLO'):
        print(result)
    else:
        [print(x.nombre) for x in result]
    tiempo=fin-inicio
    print('\nTiempo tardado:', tiempo)

def heuristica(problema, p):
    Heuristicas.problema=problema
    inicio=0
    fin=0
    result=0
    print('Para utilizar el prego introduzca 1 \nPara utilizar delta0 introduzca 2')
    option=int(input('\tIntroduzca aqui si opción: '))
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
   

def app(problema,objetivo):
    print('\nIntroduzca 1 si desea obtener la heuristica del problema\nIntroduzca 2 si desea realizar una busqueda del problema\nIntroduzca 3 para salir')
    choose=int(input('\tIntroduzca aqui su opción: '))
    if choose==1:
        print('\nHa elegido obtener la heurística')
        heuristica(problema, objetivo)
        app(problema, objetivo)
    elif choose == 2:
        print('\nHa elegido realizar una busqueda')
        busqueda(problema, objetivo)
        app(problema, objetivo)    
    elif choose == 3:
        print('Que tenga un buen día.')
    else:
        print('Ha introducido una opción inválida.')
        app(problema, objetivo)
    
 