"""

Sintaxis de Range()

range([inicio], fin, [paso])

- El inicio es 0 por defecto, sino se indica.
- El paso es 1 por defecto, si no se indica.

-La funcio range() genera una serie de numeros enteros entre
el inicio y el fin-1, con el incremento dado por el paso.
"""
# caso 1: range(fin)
print(list(range(10))) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(list(range(101))) # 0, 1, 2, ..., 100
print(list(range(32)))


# caso 2: range(inicio, fin)
print(list(range(3, 10)))
print(list(range(11, 13)))
print(list(range(1001, 1002)))

# caso 3: range(inicio, fin, paso)
print(list(range(3, 20, 2))) # 3, 5, 7, 9, 11, 13, 15, 17, 19
print(list(range(3, 21, 2)))
print(list(range(5, 5, 5)))
print(list(range(16, 25, 2)))
print(list(range(21, -10, -2)))




