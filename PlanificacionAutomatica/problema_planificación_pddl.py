import inspect
import re
import itertools
import copy
import PlanificacionAutomatica.problema_espacio_estados as probee



class Predicado:
    def __init__(self, *dominios):
        self.dominios = [] if dominios == ({},) else list(dominios)
        self.name = None
        self.signo = True
        

    def __str__(self):
        if self.name is not None:
            ans = []
            frame = inspect.currentframe().f_back
            tmp = dict(frame.f_globals.items())
            for k, var in tmp.items():
                if isinstance(var, self.__class__):
                    if hash(self) == hash(var):
                        ans.append(k)
            tmp = dict(frame.f_locals.items())
            for k, var in tmp.items():
                if isinstance(var, self.__class__):
                    if hash(self) == hash(var):
                        ans.append(k)
            self.name = ans[0]
        return self.name

    def __call__(self, *argumentos):
        if self.name is None:
            ans = []
            frame = inspect.currentframe().f_back
            tmp = dict(frame.f_globals.items())
            for k, var in tmp.items():
                if isinstance(var, self.__class__):
                    if hash(self) == hash(var):
                        ans.append(k)
            tmp = dict(frame.f_locals.items())
            for k, var in tmp.items():
                if isinstance(var, self.__class__):
                    if hash(self) == hash(var):
                        ans.append(k)
            self.name = ans[0]
        diccionario = {}
        if (len(self.dominios) == len(argumentos)): 
                # and all(arg in dom
                # for arg, dom in zip(argumentos, self.dominios)
                # if not re.fullmatch('{[^}]+}', arg))
                
                # [argumentos[i] in self.dominios[i]
                #  for i in range(len(argumentos))
                #  if not re.fullmatch('{[^}]+}',argumentos[i])])):
            diccionario[self.name] = {tuple(argumentos)}
        else:
            raise ValueError('Los argumentos no son correctos')
        return diccionario

def agrupar_diccionarios(diccionarios):
    if diccionarios is None:
        diccionarios = []
    if not isinstance(diccionarios, list):
        diccionarios = [diccionarios]
    diccionario_total = {}
    for diccionario in diccionarios:
        for key in diccionario.keys():
            if key in diccionario_total:
                diccionario_total[key].update(diccionario[key])
            else:
                diccionario_total[key] = diccionario[key]
    return diccionario_total

# Un Estado es un conjunto de ??tomos positivos cerrados que expresan los hechos
# que son ciertos. Cualquier instancia de un ??tomo que no aparezca en un estado
# se considerar?? falso.
# Ejemplo:
#    Estado({despejado(B), despejado(C), despejado(D), brazo_libre(),
#            sobre(B,A), sobre_la_mesa(C), sobre_la_mesa(D), sobre_la_mesa(A)})
# Representaci??n: Diccionario que para cada s??mbolo de predicado tiene asociado
# el conjunto de posibles tuplas que representan las instancias de dicho
# predicado que son ciertas.
# Ejemplo:
#    {'despejado' : {(B), (C), (D)},
#     'brazo_libre' : {()},
#     'sobre': {(B,A)},
#     'sobre_la_mesa': {(C), (D), (A)}}


class Estado:
    def __init__(self, *atomos):
        self.atomos = {}
        for atomo in atomos:
            for key, value in atomo.items():
                if key in self.atomos:
                    self.atomos[key] = self.atomos[key].union(value)
                else:
                    self.atomos[key] = value

    def __str__(self):
        return '\n'.join('{}({})'.format(key, ', '.join('{}'.format(arg)
                                                        for arg in valor))
                         for key, valores in self.atomos.items()
                         for valor in valores)

    def __eq__(self, otro):
        return self.atomos == otro.atomos

    def satisface_positivas(self, condiciones):
        return all(key in self.atomos.keys() and
                   value in self.atomos[key]
                   for key in condiciones.keys()
                   for value in condiciones[key])

    def satisface_negativas(self, condiciones):
        return all(key not in self.atomos.keys() or
                   value not in self.atomos[key]
                   for key in condiciones.keys()
                   for value in condiciones[key])


# -----------------------------------------------------------------------------


class Acci??nPlanificaci??n(probee.Acci??n):
    def __init__(self, nombre,
                 precondicionesP=None, precondicionesN=None,
                 efectosP=None, efectosN=None, coste=1):
        self.nombre = nombre
        self.precondicionesP = agrupar_diccionarios(precondicionesP)
        self.precondicionesN = agrupar_diccionarios(precondicionesN)
        self.efectosP = agrupar_diccionarios(efectosP)
        self.efectosN = agrupar_diccionarios(efectosN)
        self.coste = coste

    def es_aplicable(self, estado):
        return (estado.satisface_positivas(self.precondicionesP) and
                estado.satisface_negativas(self.precondicionesN))

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        for key in self.efectosN.keys():
            for value in self.efectosN[key]:
                if key in nuevo_estado.atomos.keys():
                    nuevo_estado.atomos[key].discard(value)
        for key in self.efectosP.keys():
            if key in nuevo_estado.atomos.keys():
                nuevo_estado.atomos[key].update(self.efectosP[key])
            else:
                nuevo_estado.atomos[key] = self.efectosP[key]
        return nuevo_estado

    def coste_de_aplicar(self, estado):
        return self.coste

    def __str__(self):
        return ('\nAcci??n: ' + self.nombre +
                '\n  Precondiciones:\n    ' +
                '\n    '.join(['-{}({})'.format(key, ', '.join('{}'.format(arg)
                                                for arg in valor))
                              for key, valores in self.precondicionesN.items()
                              for valor in valores] +
                              ['{}({})'.format(key, ', '.join('{}'.format(arg)
                                               for arg in valor))
                              for key, valores in self.precondicionesP.items()
                              for valor in valores]) +
                '\n  Efectos:\n    ' +
                '\n    '.join(['-{}({})'.format(key, ', '.join('{}'.format(arg)
                                                for arg in valor))
                              for key, valores in self.efectosN.items()
                              for valor in valores] +
                              ['{}({})'.format(key, ', '.join('{}'.format(arg)
                                               for arg in valor))
                              for key, valores in self.efectosP.items()
                              for valor in valores]) +
                '\n  Coste: ' + str(self.coste))


# -----------------------------------------------------------------------------


def instanciar(diccionario, asignaci??n):
    instancia = {}
    for key in diccionario:
        instancia[key] = set()
        for value in diccionario[key]:
            instancia[key].update({tuple(argumento.format(**asignaci??n)
                                         for argumento in value)})
        if instancia[key] == set():
            instancia[key] = {()}
    return instancia


class EsquemaPlanificaci??n:
    def __init__(self, nombre,
                 precondicionesP=None, precondicionesN=None,
                 efectosP=None, efectosN=None,
                 coste=None, dominio=None, variables=None):
        self.nombre = nombre
        self.nombres_variables = re.findall('{([^}]*)}', nombre)
        self.precondicionesP = agrupar_diccionarios(precondicionesP)
        self.precondicionesN = agrupar_diccionarios(precondicionesN)
        self.efectosP = agrupar_diccionarios(efectosP)
        self.efectosN = agrupar_diccionarios(efectosN)
        self.dominio = dominio
        self.variables = variables
        if coste is None or isinstance(coste, int):
            coste = CosteEsquema(coste)()
        self.coste_esquema = coste

    def obtener_acci??n(self, asignaci??n):
        nombre = self.nombre.format(**asignaci??n)
        precondicionesP = instanciar(self.precondicionesP, asignaci??n)
        precondicionesN = instanciar(self.precondicionesN, asignaci??n)
        efectosP = instanciar(self.efectosP, asignaci??n)
        efectosN = instanciar(self.efectosN, asignaci??n)
        coste = self.coste_esquema.coste(asignaci??n)
        return Acci??nPlanificaci??n(
                nombre, precondicionesP, precondicionesN,
                efectosP, efectosN, coste)

    def obtener_acciones(self):
        if self.dominio is None:
            valores_variables = [self.variables[key]
                                 for key in self.nombres_variables
                                 if key in self.variables.keys()]
            producto_valores = itertools.product(*valores_variables)
            asignaciones = (dict(zip(self.nombres_variables, valores))
                            for valores in producto_valores)
        else:
            asignaciones = (dict(zip(self.nombres_variables, valores))
                            for valores in self.dominio)
        return [self.obtener_acci??n(asignaci??n)
                for asignaci??n in asignaciones]

    def __str__(self):
        acciones = self.obtener_acciones()
        return ('Operador: ' + self.nombre +
                '\nACCIONES GENERADAS:\n' +
                '\n'.join(str(acci??n) for acci??n in acciones))


# -----------------------------------------------------------------------------


class CosteEsquema:
    def __init__(self, coste=None):
        if coste is None:
            coste = 1
        if isinstance(coste, int):
            def funci??n_coste(*argumentos):
                return coste
            self.funci??n_coste = funci??n_coste
        else:
            self.funci??n_coste = coste

    def coste(self, asignaci??n):
        return self.funci??n_coste(*(argumento.format(**asignaci??n)
                                    for argumento in self.argumentos))

    def __call__(self, *argumentos):
        coste_esquema = copy.deepcopy(self)
        coste_esquema.argumentos = argumentos
        return coste_esquema


# -----------------------------------------------------------------------------


class ProblemaPlanificaci??n(probee.ProblemaEspacioEstados):
    def __init__(self, operadores, estado_inicial,
                 objetivosP=None, objetivosN=None):
        self.objetivosP = agrupar_diccionarios(objetivosP)
        self.objetivosN = agrupar_diccionarios(objetivosN)
        if not isinstance(operadores, list):
            operadores = [operadores]
        acciones = sum(([operador] if isinstance(operador, Acci??nPlanificaci??n)
                       else operador.obtener_acciones()
                       for operador in operadores), [])
        super().__init__(acciones, estado_inicial)

    def es_estado_final(self, estado):
        return (estado.satisface_positivas(self.objetivosP) and
                estado.satisface_negativas(self.objetivosN))
