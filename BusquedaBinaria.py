def busqueda_binaria_iterativa(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

def busqueda_binaria_recursiva(lista, objetivo, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1

    if inicio > fin:
        return -1

    medio = (inicio + fin) // 2

    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, fin)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, inicio, medio - 1)

if __name__ == "__main__":
    datos = [1, 3, 5, 7, 9, 11, 13, 15]
    objetivo = 7

    resultado_iter = busqueda_binaria_iterativa(datos, objetivo)
    print(f"Búsqueda Iterativa: El elemento está en la posición {resultado_iter}")

    resultado_rec = busqueda_binaria_recursiva(datos, objetivo)
    print(f"Búsqueda Recursiva: El elemento está en la posición {resultado_rec}")