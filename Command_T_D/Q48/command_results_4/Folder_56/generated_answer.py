
def return_binary_or_hexa(test_tup):
    res = ""
    a, b = test_tup[7], test_tup[9]
    suma = a + 1
    sumb = b - 1
    if a <= suma <= sumb:
        res += str(suma)
        suma += 1
        sumb -= 1
    while suma <= sumb:
        if suma not in test_tup:
            res += str(suma)
            suma += 1
        elif sumb not in test_tup:
            res += str(sumb)
            sumb -= 1
        suma += 1
        sumb -= 1
    if res:
        if res % 2 == 1:
            res = bin(int(res))
        else:
            res = hex(int(res))
    return res
