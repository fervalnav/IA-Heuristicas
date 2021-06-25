# import PlanificacionAutomatica.problema_planificación_pddl as probpl
# import PlanificacionAutomatica.búsqueda_espacio_estados as búsqee
# import Heuristicas
# import Prego
# import auxiliares


# cuevas = {f'C{i}' for i in range(5)}
# buceadores = {f'B{i}' for i in range(2)}
# cantidades = {str(i) for i in range(9)}
# tanques = {str(i) for i in range(5)}

# print("Cuevas: {}".format(cuevas))
# print("Buceadores: {}".format(buceadores))
# print("Tanques: {}".format(tanques))
# print("Cantidades: {}".format(cantidades))

# conexiones = [('C0', 'C1'),
#               ('C1', 'C0'),
#               ('C1', 'C2'),
#               ('C1', 'C4'),
#               ('C2', 'C1'),
#               ('C2', 'C3'),
#               ('C3', 'C2'),
#               ('C4', 'C1')]

# posicion_buceador = probpl.Predicado(buceadores, cuevas | {'superficie'})
# disponible = probpl.Predicado(buceadores)
# trabajando = probpl.Predicado(buceadores)
# descompresion = probpl.Predicado(buceadores)
# tanques_llenos = probpl.Predicado(buceadores | cuevas, cantidades)
# con_foto_de = probpl.Predicado(cuevas)

# contratar_B0 = probpl.AcciónPlanificación(
#     nombre = 'contratar(B0)',
#     precondicionesP= disponible('B0'),
#     precondicionesN= trabajando('B0'),
#     efectosN=[disponible('B0'), disponible('B1')],
#     efectosP=trabajando('B0'),
#     coste = 10
# )

# contratar_B1 = probpl.AcciónPlanificación(
#     nombre = 'contratar(B1)',
#     precondicionesP= disponible('B1'),
#     precondicionesN= trabajando('B1'),
#     efectosN=[disponible('B1'), disponible('B0')],
#     efectosP=trabajando('B1'),
#     coste = 67
# )


import PlanificacionAutomatica.problema_planificación_pddl as probpl
import PlanificacionAutomatica.búsqueda_espacio_estados as búsqee
import Heuristicas
import Prego
import auxiliares

cuevas = {f'C{i}' for i in range(5)}
buceadores = {f'B{i}' for i in range(2)}
cantidades = {str(i) for i in range(9)}

conexiones = [('C0', 'C1'),
              ('C1', 'C0'),
              ('C1', 'C2'),
              ('C1', 'C4'),
              ('C2', 'C1'),
              ('C2', 'C3'),
              ('C3', 'C2'),
              ('C4', 'C1')]

posicion_buceador = probpl.Predicado(buceadores, cuevas | {'superficie'})
disponible = probpl.Predicado(buceadores)
trabajando = probpl.Predicado(buceadores)
descompresion = probpl.Predicado(buceadores)
tanques_llenos = probpl.Predicado(buceadores | cuevas, cantidades)
con_foto_de = probpl.Predicado(cuevas)

auxiliares.predicados=[posicion_buceador,disponible,trabajando,descompresion,tanques_llenos,con_foto_de]

contratar_B0 = probpl.AcciónPlanificación(
    nombre = 'contratar(B0)',
    precondicionesP = disponible('B0'),
    precondicionesN = trabajando('B1'),
    efectosN = [disponible('B0'), disponible('B1')],
    efectosP = trabajando('B0'),
    coste = 10
)
contratar_B1 = probpl.AcciónPlanificación(
    nombre = 'contratar(B1)',
    precondicionesP = disponible('B1'),
    precondicionesN = trabajando('B0'),
    efectosN = disponible('B1'),
    efectosP = trabajando('B1'),
    coste = 67
)
contratar = probpl.EsquemaPlanificación(
    nombre = 'contratar({b})',
    precondicionesP = disponible('{b}'),
    efectosN = disponible('{b}'),
    efectosP = trabajando('{b}'),
    variables = {'b': buceadores})

entrar_al_agua = probpl.EsquemaPlanificación(
    nombre = 'entrar_al_agua({b})',
    precondicionesP = [trabajando('{b}'),
                       posicion_buceador('{b}', 'superficie')],
    efectosN = posicion_buceador('{b}', 'superficie'),
    efectosP = [posicion_buceador('{b}', 'C0'),
                tanques_llenos('{b}', '4')],
    variables = {'b': buceadores})

bucear = probpl.EsquemaPlanificación(
    nombre = 'bucear({b}, {c1}, {c2}, {t1}, {t2})',
    precondicionesP = [posicion_buceador('{b}', '{c1}'),
                      tanques_llenos('{b}','{t1}')],
    efectosN = [posicion_buceador('{b}', '{c1}'),
               tanques_llenos('{b}', '{t1}')],
    efectosP = [posicion_buceador('{b}', '{c2}'),
               tanques_llenos('{b}', '{t2}')],
    dominio = [(b, c1, c2, str(t1), str(t1 -1)) for b in buceadores
              for (c1, c2) in conexiones
              for t1 in range(1, 5)]
)
fotografiar = probpl.EsquemaPlanificación(
    nombre = 'fotografiar({b}, {c}, {t1}, {t2})',
    precondicionesP = [posicion_buceador('{b}', '{c}'),
                     tanques_llenos('{b}', '{t1}')],
    efectosN = [tanques_llenos('{b}', '{t1}')],
    efectosP = [tanques_llenos('{b}', '{t2}'),
               con_foto_de('{c}')],
    dominio = [(b, c, str(t1), str(t1 -1)) for b in buceadores
              for c in cuevas
              for t1 in range(1, 5)]
)
soltar_tanque = probpl.EsquemaPlanificación(
    nombre = 'soltar_tanque({b}, {c}, {t1}, {t2}, {t3}, {t4})',
    precondicionesP = [posicion_buceador('{b}', '{c}'),
                       tanques_llenos('{b}', '{t1}'),
                       tanques_llenos('{c}', '{t2}')],
    efectosN = [tanques_llenos('{b}', '{t1}'),
               tanques_llenos('{c}', '{t2}')],
    efectosP = [tanques_llenos('{b}', '{t3}'),
               tanques_llenos('{c}', '{t4}')],
    dominio = [(b, c, str(t1), str(t2), str(t1 -1), str(t2 + 1)) for b in buceadores
              for c in cuevas
              for t1 in range(1, 5)
              for t2 in range(8)]
)
cargar_tanque = probpl.EsquemaPlanificación(
    nombre = 'cambiar_tanque({b}, {c}, {t1}, {t2}, {t3}, {t4})',
    precondicionesP = [posicion_buceador('{b}', '{c}'),
                      tanques_llenos('{b}', '{t1}'),
                      tanques_llenos('{c}', '{t2}')] ,
    efectosN = [tanques_llenos('{b}', '{t1}'),
               tanques_llenos('{c}', '{t2}')],
    efectosP = [tanques_llenos('{b}', '{t3}'),
               tanques_llenos('{c}', '{t4}')],
    dominio = [(b, c, str(t1), str(t2), str(t1 + 1), str(t2 - 1)) for b in buceadores
              for c in cuevas
              for t1 in range(1, 4)
              for t2 in range(1, 9)]
)

salir_del_agua = probpl.EsquemaPlanificación(
    nombre = 'salir_del_agua({b})',
    precondicionesP = [posicion_buceador('{b}', 'C0')],
    efectosN = [posicion_buceador('{b}', 'C0'),
               trabajando('{b}')],
    efectosP = [posicion_buceador('{b}', 'superficie'),
               descompresion('{b}')],
    variables = {'b': buceadores}
)

estado_inicial_buceadores = probpl.Estado(
    posicion_buceador('B0', 'superficie'),
    posicion_buceador('B1', 'superficie'),
    tanques_llenos('C0', '0'),
    tanques_llenos('C1', '0'),
    tanques_llenos('C2', '0'),
    tanques_llenos('C3', '0'),
    tanques_llenos('C4', '0'),
    disponible('B0'),
    disponible('B1'))

problema_buceadores = probpl.ProblemaPlanificación(
    operadores = [contratar,
                 entrar_al_agua, bucear, fotografiar,
                 cargar_tanque, soltar_tanque, salir_del_agua],
    estado_inicial = estado_inicial_buceadores,
    objetivosP = [posicion_buceador('B0', 'superficie'),
                 posicion_buceador('B1', 'superficie'),
                 con_foto_de('C4')])


# print(f'Estado inicial:\n{estado_inicial_buceadores}')
# print(f'Objetivos positivos: {problema_buceadores.objetivosP}')
# print(f'Objetivos negativos: {problema_buceadores.objetivosN}')
# busqueda_profundidad = búsqee.BúsquedaEnProfundidadAcotada(cota=15)
# print('Busqueda en profundidad: ', busqueda_profundidad.buscar(problema_buceadores))

Prego.problema=problema_buceadores

objetivosP = [posicion_buceador('B0', 'superficie'),
            posicion_buceador('B1', 'superficie'),
            con_foto_de('C4')]
result = 0
for objetivo in objetivosP:
    result += Prego.nuevoIntento(estado_inicial_buceadores, objetivo)


print('-------------------------Result-------------------------')
# [print(x.nombre) for x in result]
print(result)

# Heuristicas.problema=problema_buceadores
# result =0
# for objetivo in objetivosP:
#     result += Heuristicas.heuristica(estado_inicial_buceadores, objetivo)
# print(result)