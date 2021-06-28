
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

def incluyeEfectos(p, acciones, usadas=[]):
    lista = []
    for accion in acciones:
        for clave in p:
            if clave in accion.efectosP.keys() and p[clave]==accion.efectosP[clave]:
                lista.append(accion)

    for uso in usadas:
        if uso in lista:
            lista.remove(uso)
    return lista

def parseObjetivos(objetivos):
    res = []
    for (k,values) in objetivos.items():
        for v in values:
            res.append(get_predicado(k,[v]))
    return res