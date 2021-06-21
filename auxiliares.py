
predicados=[]

def get_predicado(name, listaArg):
    for predicado in predicados:
        if predicado.name==name: 
            if len(predicado.dominios) == 0:
                return predicado()
            else:
                lista = []
                [lista.append(letra) for letra in listaArg]
                return predicado(*lista[0])

def incluyeEfectos(p, acciones):
    lista = []
    for accion in acciones:
        for clave in p:
            if clave in accion.efectosP.keys() and p[clave]==accion.efectosP[clave]:
                lista.append(accion)
    return lista
