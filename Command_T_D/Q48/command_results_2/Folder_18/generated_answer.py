
def return_binary_or_hexa(test_tup):
    a, b = test_tup[56], test_tup[90]
    suma = 0
    for i in range(a + 1, b):
        if i not in test_tup[56:90]:
            suma += i
    if suma % 2:
        return f'{suma:b}'
    else:
        return f'{suma:x}'
