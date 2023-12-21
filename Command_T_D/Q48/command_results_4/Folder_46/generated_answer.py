
def return_binary_or_hexa(test_list):
    a = test_list[10]
    b = test_list[79]
    suma = 0
    for i in range(a + 1, b):
        if i not in test_list:
            suma += i
    if suma % 2 == 0:
        return hex(suma)
    else:
        return bin(suma)
