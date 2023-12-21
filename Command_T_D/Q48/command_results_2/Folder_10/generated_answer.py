
def return_binary_or_hexa(test_tup):
    test_tup = set(test_tup)
    suma = 0
    test_tup_set_len = len(test_tup)
    if (test_tup_set_len > 0):
        suma += test_tup[test_tup_set_len - 1] - test_tup[test_tup_set_len - 2]
    if (suma % 2 == 1):
        return format(suma, 'b')
    else:
        return format(suma, 'x')
