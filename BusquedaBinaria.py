def buslineal(lis, busca):
    global ops
    for x in lis:
        ops+=1
        if x == busca:
            return True
    return False

def busbinaria(lis, busca):
    pass

ops = 0
a=[1,3,6,9,4]
print(buslineal(a,6), ops)
ops = 0
print(buslineal(a,8), ops)