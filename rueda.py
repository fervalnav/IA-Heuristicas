import PlanificacionAutomatica.problema_planificación_pddl as probpl
import PlanificacionAutomatica.búsqueda_espacio_estados as búsqee
import Prego
import Heuristicas
import auxiliares

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
    objetivosP=[en('rueda-pinchada', 'maletero'),
                en('rueda-repuesto', 'eje')]
)


auxiliares.predicados = [en]

Prego.problema=problema_rueda_pinchada

result = Prego.prego(estado_inicial_rueda, en('rueda-repuesto', 'eje')) + Prego.prego(estado_inicial_rueda, en('rueda-pinchada', 'maletero'))

print('-------------------------Result-------------------------')
[print(x.nombre) for x in result]

Heuristicas.problema=problema_rueda_pinchada

heur=Heuristicas.heuristica(estado_inicial_rueda,en('rueda-repuesto', 'eje')) + Heuristicas.heuristica(estado_inicial_rueda, en('rueda-pinchada', 'maletero'))
print('Heuristica: ', heur)