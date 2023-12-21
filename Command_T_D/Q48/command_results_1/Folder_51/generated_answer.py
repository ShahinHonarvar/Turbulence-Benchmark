
def return_binary_or_hexa(test_list):
    a, b = test_list[6], test_list[9]
    suma = a + 1
    sumb = b - 1
    suma = suma + sumb - len(test_list[6:9])
    if suma % 2 == 1:
        return format(suma, "b")
    else:
        return format(suma, "x")
