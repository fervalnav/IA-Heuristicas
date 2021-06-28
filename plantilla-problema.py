import PlanificacionAutomatica.problema_planificación_pddl as probpl
import PlanificacionAutomatica.búsqueda_espacio_estados as búsqee
import auxiliares
import app


variables = None

predicado1 = None
predicado2 = None

coste_bloque = probpl.CosteEsquema()

accion1 = probpl.AcciónPlanificación(
    nombre='accion1',
    precondicionesP=None,
    efectosP=None,
    efectosN=None
)

esquema_accion1 = probpl.EsquemaPlanificación(
    nombre='accion2({x}, {y})',
    precondicionesP=None,
    efectosN=[None],
    efectosP=[None],
    coste=coste_bloque('{x}'),
    dominio={(x, y) for x in variables for y in variables if x != y}
)

esquema_accion2 = probpl.EsquemaPlanificación(
    nombre='accion3({x}, {y})',
    precondicionesP=[None],
    efectosN=[None],
    efectosP=[None],
    coste=coste_bloque('{x}'),
    dominio={(x, y) for x in variables for y in variables if x != y}
)



auxiliares.predicados = [predicado1, predicado2]

estado_inicial = probpl.Estado(
    predicado1, predicado2
)

problema = probpl.ProblemaPlanificación(
    operadores=[accion1,
                esquema_accion1('x','y'),
                esquema_accion2('c','d')],
    estado_inicial=estado_inicial,
    objetivosP=[predicado1]
)




app.app(problema)
