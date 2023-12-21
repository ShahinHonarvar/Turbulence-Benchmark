
def return_binary_or_hexa(test_list):
    a, b = test_list[44], test_list[67]
    suma = sum(range(a + 1, b))
    if suma % 2 == 1:
        return format(suma, 'b')
    else:
        return format(suma, 'x')
