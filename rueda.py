from busquedas import busqueda_en_profundidad_H
import PlanificacionAutomatica.problema_planificación_pddl as probpl
import PlanificacionAutomatica.búsqueda_espacio_estados as búsqee
import Heuristicas
import auxiliares
import app

ruedas = {'rueda-pinchada', 'rueda-repuesto'}
localizaciones = {'eje', 'maletero', 'suelo'}
en = probpl.Predicado(ruedas, localizaciones)

estado_inicial_rueda = probpl.Estado(en('rueda-pinchada', 'eje'),
                                     en('rueda-repuesto', 'maletero'))

# Sacar la rueda de repuesto del maletero
sacar = probpl.AcciónPlanificación(
    nombre='sacar_repuesto',
    precondicionesP=en('rueda-repuesto', 'maletero'),
    efectosP=en('rueda-repuesto', 'suelo'),
    efectosN=en('rueda-repuesto', 'maletero')
)

# Quitar la rueda pinchada del eje
quitar = probpl.AcciónPlanificación(
    nombre='quitar_pinchada',
    precondicionesP=en('rueda-pinchada', 'eje'),
    efectosP=en('rueda-pinchada', 'suelo'),
    efectosN=en('rueda-pinchada', 'eje')
)

# Colocar la rueda de repuesto en el eje
poner = probpl.AcciónPlanificación(
    nombre='poner_repuesto',
    precondicionesP=en('rueda-repuesto', 'suelo'),
    precondicionesN=en('rueda-pinchada', 'eje'),
    efectosP=en('rueda-repuesto', 'eje'),
    efectosN=en('rueda-repuesto', 'suelo')
)

# Guardar la rueda pinchada en el maletero
guardar = probpl.AcciónPlanificación(
    nombre='guardar_pinchada',
    precondicionesP=en('rueda-pinchada', 'suelo'),
    precondicionesN=en('rueda-repuesto', 'maletero'),
    efectosP=en('rueda-pinchada', 'maletero'),
    efectosN=en('rueda-pinchada', 'suelo')
)

problema_rueda_pinchada = probpl.ProblemaPlanificación(
    operadores=[quitar, guardar, sacar, poner],
    estado_inicial=estado_inicial_rueda,
    objetivosP = [en('rueda-repuesto', 'maletero'),en('rueda-pinchada', 'eje')]
)

# print(f'Estado inicial:\n{estado_inicial_rueda}')
# print(f'Objetivos positivos: {problema_rueda_pinchada.objetivosP}')
# print(f'Objetivos negativos: {problema_rueda_pinchada.objetivosN}')
# busqueda_profundidad = búsqee.BúsquedaEnProfundidad()
# print('Busqueda en profundidad: ', busqueda_profundidad.buscar(problema_rueda_pinchada))


auxiliares.predicados = [en]


# result = Prego.nuevoIntento(estado_inicial_rueda, en('rueda-repuesto', 'eje')) + Prego.nuevoIntento(estado_inicial_rueda, en('rueda-pinchada', 'maletero'))

# print('-------------------------Result-------------------------')
# # [print(x.nombre) for x in reversed(result)]
# print(result)

objetivosP = [en('rueda-repuesto', 'maletero'),en('rueda-pinchada', 'eje')]
# resultado = busqueda_en_profundidad_H(estado_inicial_rueda, objetivosP, problema_rueda_pinchada.acciones)
# print('-----Result-----')
# [print(x.nombre) for x in resultado]


# Heuristicas.problema=problema_rueda_pinchada

# heur=Heuristicas.heuristica(estado_inicial_rueda,en('rueda-repuesto', 'eje')) + Heuristicas.heuristica(estado_inicial_rueda, en('rueda-pinchada', 'maletero'))
# print('Heuristica: ', heur)

# app.busqueda(problema_rueda_pinchada, objetivosP)
app.heuristica(problema_rueda_pinchada, objetivosP)