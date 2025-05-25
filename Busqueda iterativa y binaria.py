ops = 0
def busbinaria_iterativa(lis, busca):
    global ops
    ini = 0
    fin = len(lis) - 1
    while ini <= fin:
        ops += 1
        mid = (ini + fin) // 2
        if lis[mid] == busca:
            return True
        elif busca < lis[mid]:
            fin = mid - 1
        else:
            ini = mid + 1
    return False

def busbinaria_recursiva(lis, busca, ini, fin):
    global ops
    if ini > fin:
        return False
    ops += 1
    mid = (ini + fin) // 2
    if lis[mid] == busca:
        return True
    elif busca < lis[mid]:
        return busbinaria_recursiva(lis, busca, ini, mid - 1)
    else:
        return busbinaria_recursiva(lis, busca, mid + 1, fin)
    
a=[1,3,4,6,9]


print("Lista ordenada:", a)

ops = 0
print( busbinaria_iterativa(a, 6), "Ops:", ops)

ops = 0
print(busbinaria_iterativa(a, 8), "Ops:", ops)

ops = 0
print(busbinaria_recursiva(a, 6, 0, len(a) - 1), "Ops:", ops)

ops = 0
print(busbinaria_recursiva(a, 8, 0, len(a) - 1), "Ops:", ops)