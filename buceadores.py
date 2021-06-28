from busquedas import busqueda_en_profundidad_H
import PlanificacionAutomatica.problema_planificación_pddl as probpl
import PlanificacionAutomatica.búsqueda_espacio_estados as búsqee
import auxiliares
import app

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
    tanques_llenos('C0', '4'),
    tanques_llenos('C1', '4'),
    tanques_llenos('C2', '2'),
    tanques_llenos('C3', '2'),
    tanques_llenos('C4', '2'),
    disponible('B0'),
    disponible('B1'))

problema_buceadores1 = probpl.ProblemaPlanificación(
    operadores = [contratar,
                 entrar_al_agua, bucear, fotografiar,
                 cargar_tanque, soltar_tanque, salir_del_agua],
    estado_inicial = estado_inicial_buceadores,
    objetivosP = [posicion_buceador('B0', 'superficie'),
                 posicion_buceador('B1', 'superficie'),
                 con_foto_de('C1')])

problema_buceadores2 = probpl.ProblemaPlanificación(
    operadores = [contratar,
                 entrar_al_agua, bucear, fotografiar,
                 cargar_tanque, soltar_tanque, salir_del_agua],
    estado_inicial = estado_inicial_buceadores,
    objetivosP = [posicion_buceador('B0', 'superficie'),
                 posicion_buceador('B1', 'superficie'),
                 con_foto_de('C1')])



app.app(problema_buceadores1)