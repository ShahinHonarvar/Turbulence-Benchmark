
def return_binary_or_hexa(test_list):
    a, b = test_list[6], test_list[7]
    suma = sum(x for x in range(a + 1, b - 1) if x not in test_list[6:7])
    if suma % 2 == 0:
        return hex(suma)
    else:
        return f'{suma:b}'
