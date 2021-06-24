import PlanificacionAutomatica.problema_planificación_pddl as probpl
import PlanificacionAutomatica.búsqueda_espacio_estados as búsqee
import Heuristicas
import Prego
import auxiliares


cuevas = {f'C{i}' for i in range(5)}
buceadores = {f'B{i}' for i in range(2)}
cantidades = {str(i) for i in range(9)}
tanques = {str(i) for i in range(5)}

print("Cuevas: {}".format(cuevas))
print("Buceadores: {}".format(buceadores))
print("Tanques: {}".format(tanques))
print("Cantidades: {}".format(cantidades))

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

contratar_B0 = probpl.AcciónPlanificación(
    nombre = 'contratar(B0)',
    precondicionesP= disponible('B0'),
    precondicionesN= trabajando('B0'),
    efectosN=[disponible('B0'), disponible('B1')],
    efectosP=trabajando('B0'),
    coste = 10
)

contratar_B1 = probpl.AcciónPlanificación(
    nombre = 'contratar(B1)',
    precondicionesP= disponible('B1'),
    precondicionesN= trabajando('B1'),
    efectosN=[disponible('B1'), disponible('B0')],
    efectosP=trabajando('B1'),
    coste = 67
)