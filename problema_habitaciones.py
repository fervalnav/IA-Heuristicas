from busquedas import busqueda_en_profundidad_H
import PlanificacionAutomatica.problema_planificación_pddl as probpl
import PlanificacionAutomatica.búsqueda_espacio_estados as búsqee
import Prego
import Heuristicas
import auxiliares

cajas = {'C1', 'C2'}
habitaciones = {'H1', 'H2', 'H3'}
puertas = {'P1', 'P2'}

abierta = probpl.Predicado(puertas)
en = probpl.Predicado(cajas, habitaciones)
roboten = probpl.Predicado(habitaciones)
conecta = probpl.Predicado(puertas, habitaciones, habitaciones)

estado_inicial_habitaciones = probpl.Estado(abierta('P1'),
                                            en('C1', 'H1'),
                                            roboten('H1'),
                                            conecta('P1','H1','H2'),
                                            conecta('P2','H2','H3'))

irVia = probpl.EsquemaPlanificación(
    nombre='irVia({p}, {x}, {y})',
    precondicionesP=[abierta('{p}'),
                     roboten('{x}'),
                     conecta('{p}', '{x}', '{y}')],
    efectosN=roboten('{x}'),
    efectosP=roboten('{y}'),
    #variables={'p': puertas,'x': habitaciones,'y': habitaciones}
    dominio={('P1','H1','H2'), ('P1','H2','H1'), ('P2','H2','H3'), ('P2','H3','H2')}
)

desplazarVia = probpl.EsquemaPlanificación(
    nombre='desplazarVia({c}, {p}, {x}, {y})',
    precondicionesP=[abierta('{p}'),
                     en('{c}', '{x}'),
                     roboten('{x}'),
                     conecta('{p}', '{x}', '{y}')],
    efectosN=[roboten('{x}'),
              en('{c}', '{x}')],
    efectosP=[roboten('{y}'),
              en('{c}', '{y}')],
    #variables={'p': puertas,'x': habitaciones,'y': habitaciones,'c': cajas}
    dominio={('C1','P1','H1','H2'), ('C1','P1','H2','H1'), ('C1','P2','H2','H3'), ('C1','P2','H3','H2'),
                ('C2','P1','H1','H2'), ('C2','P1','H2','H1'), ('C2','P2','H2','H3'), ('C2','P2','H3','H2')}
)

cerrar = probpl.EsquemaPlanificación(
    nombre='cerrar({p}, {x})',
    precondicionesP=[abierta('{p}'), roboten('{x}')],
    efectosN=abierta('{p}'),
    #variables={'p': puertas, 'x': habitaciones}
    dominio={('P1','H1'), ('P1','H2'), ('P2','H2'), ('P2','H3')}
)

abrir = probpl.EsquemaPlanificación(
    nombre='abrir({p}, {x})',
    precondicionesP=roboten('{x}'),
    precondicionesN=abierta('{p}'),
    efectosP=abierta('{p}'),
    #variables={'p': puertas,'x': habitaciones}
    dominio={('P1','H1'), ('P1','H2'), ('P2','H2'), ('P2','H3')}
)

problema_habitaciones = probpl.ProblemaPlanificación(
    operadores=[irVia,desplazarVia,abrir,cerrar],
    estado_inicial=estado_inicial_habitaciones,
    objetivosP=[abierta('P2'),
                en('C1', 'H3'),
                roboten('H3')]
)

auxiliares.predicados = [abierta, en, roboten, conecta]
Prego.problema=problema_habitaciones
objetivos1=[abierta('P2'),
                en('C1', 'H3'),
                roboten('H3')]

resultado = busqueda_en_profundidad_H(estado_inicial_habitaciones, objetivos1, problema_habitaciones.acciones)
print('-----Result-------')
[print(x.nombre) for x in resultado]