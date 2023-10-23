numeros= {1, 2, 3, 4}
numeros.remove(3)
print(numeros)

numeros = {1, 2, 3, 4, 5}
numeros.discard(5)
numeros.add(6)
print(numeros)

numeros = {1, 2, 3}
print(2 in numeros) #True
print(4 in numeros) #False

a = {1, 2, 3}
b = {3, 4, 5}
c = a.union(b)
print(c)

a = {1, 2, 3}
b = {2, 3, 4}
c = a.intersection(b)
print(c)