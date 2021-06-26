from busquedas import busqueda_en_profundidad_H
import PlanificacionAutomatica.problema_planificación_pddl as probpl
import PlanificacionAutomatica.búsqueda_espacio_estados as búsqee
import Heuristicas
import Prego
import auxiliares



bloques = {'A', 'B', 'C'}
despejado = probpl.Predicado(bloques)
brazolibre = probpl.Predicado({})
sobrelamesa = probpl.Predicado(bloques)
sobre = probpl.Predicado(bloques, bloques)
agarrado = probpl.Predicado(bloques)

auxiliares.predicados = [despejado, brazolibre, sobrelamesa, sobre, agarrado]


estado_inicial_bloques = probpl.Estado(
    sobrelamesa('A'), despejado('A'),
    sobrelamesa('B'),
    sobre('C','B'), despejado('C'),
    brazolibre()
)

coste_bloque = probpl.CosteEsquema(lambda b: {'A': 1, 'B': 2, 'C': 3}[b])




# El brazo robótico coloca un bloque sobre otro bloque
apilar = probpl.EsquemaPlanificación(
    nombre='apilar({x}, {y})',
    precondicionesP=[agarrado('{x}'),
                     despejado('{y}')],
    efectosN=[agarrado('{x}'),
              despejado('{y}')],
    efectosP=[brazolibre(),
              sobre('{x}', '{y}'),
              despejado('{x}')],
    coste=coste_bloque('{x}'),
    dominio={(x, y) for x in bloques for y in bloques if x != y}
)

# El brazo robótico coge un bloque que está sobre otro bloque
desapilar = probpl.EsquemaPlanificación(
    nombre='desapilar({x}, {y})',
    precondicionesP=[brazolibre(),
                     sobre('{x}', '{y}'),
                     despejado('{x}')],
    efectosN=[brazolibre(),
              sobre('{x}', '{y}'),
              despejado('{x}')],
    efectosP=[agarrado('{x}'),
              despejado('{y}')],
    coste=coste_bloque('{x}'),
    dominio={(x, y) for x in bloques for y in bloques if x != y}
)

# El brazo robótico coge un bloque que está sobre la mesa
agarrar = probpl.EsquemaPlanificación(
    nombre='agarrar({x})',
    precondicionesP=[brazolibre(),
                     sobrelamesa('{x}'),
                     despejado('{x}')],
    efectosN=[brazolibre(),
              sobrelamesa('{x}'),
              despejado('{x}')],
    efectosP=agarrado('{x}'),
    coste=coste_bloque('{x}'),
    variables={'x': bloques}
)

# El brazo robótico deja un bloque sobre la mesa
bajar = probpl.EsquemaPlanificación(
    nombre='bajar({x})',
    precondicionesP=agarrado('{x}'),
    efectosN=agarrado('{x}'),
    efectosP=[brazolibre(),
              sobrelamesa('{x}'),
              despejado('{x}')],
    coste=coste_bloque('{x}'),
    variables={'x': bloques}
)


problema_mundo_bloques = probpl.ProblemaPlanificación(
    operadores=[apilar,
                desapilar,
                agarrar,
                bajar],
    estado_inicial=estado_inicial_bloques,
    objetivosP=[sobrelamesa('A'), despejado('A'),
    sobrelamesa('B'),
    sobre('C','B'), despejado('C'),
    brazolibre()]
)

problema_mundo_bloques2 = probpl.ProblemaPlanificación(
    operadores=[apilar,
                desapilar,
                agarrar,
                bajar],
    estado_inicial=estado_inicial_bloques,
    objetivosP=[sobrelamesa('C'),
                sobre('B', 'C'),
                sobre('A', 'B')]
)

problema_mundo_bloques3 = probpl.ProblemaPlanificación(
    operadores=[apilar,
                desapilar,
                agarrar,
                bajar],
    estado_inicial=estado_inicial_bloques,
    objetivosP=[sobrelamesa('A'), despejado('A'),
    sobrelamesa('B'), despejado('B'),
    agarrado('C')]
)
# print(f'Estado inicial:\n{estado_inicial_bloques}')
# print(f'Objetivos positivos: {problema_mundo_bloques.objetivosP}')
# print(f'Objetivos negativos: {problema_mundo_bloques.objetivosN}')
# busqueda_profundidad = búsqee.BúsquedaEnProfundidad()
# print('Busqueda en profundidad: ', busqueda_profundidad.buscar(problema_mundo_bloques))






Prego.problema=problema_mundo_bloques
objetivos = []
# for k, vSet in problema_mundo_bloques.objetivosP:
#         for v in vSet:
#             objetivos.append()
objetivos1=[sobrelamesa('C'),
                sobre('B', 'C'),
                sobre('A', 'B')]
result = 0

# for objetivo in objetivos1:
#     result +=  Prego.nuevoIntento(estado_inicial_bloques, objetivo)
# print('-------------------------Result-------------------------')
# # [print(x.nombre) for x in result]
# print(result)

resultado = busqueda_en_profundidad_H(estado_inicial_bloques, objetivos1, problema_mundo_bloques.acciones)
print('-----Result-------')
[print(x.nombre) for x in resultado]
# Heuristicas.problema=problema_mundo_bloques
# predicado = sobre('A', 'B')
# heur=Heuristicas.heuristica(estado_inicial_bloques, predicado)
# print(heur)
    


