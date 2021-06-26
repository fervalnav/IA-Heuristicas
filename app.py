import busquedas
import Prego

def aplicacion(problema):
    print('Introduzca 1 para búsqueda a ciegas \nIntroduzca 2 para búsqueda con heurística')
    choose=int(input('Introduzca aqui su opción: '))
    if(choose==1):
        print('Busqueda a ciegas')
    elif(choose==2):
        print('Has eligido búsqueda con heurística:\n\tPara utilizar el prego introduzca 1 \n\tPara utilizar delta0 introduzca 2')
        option=int(input('Introduzca aqui si opción: '))
        if(option==1):
            print('Prego')
            # result=busquedas.busqueda_en_profundidad_H(problema.estado_inicial, problema.objetivosP, problema.acciones)
            # print('-----Result-------')
            # [print(x.nombre) for x in result]
        elif(option==2):
            print('Delta 0')
        else:
           print('No has insertado opción válida')
    else:
        print('No has insertado opción válida')



