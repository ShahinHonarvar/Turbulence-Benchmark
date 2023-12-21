
def return_binary_or_hexa(test_tup):
    a, b = test_tup[48], test_tup[76]
    s = sum(x for x in range(a + 1, b - 1) if x not in test_tup[48:76])
    if s % 2:
        return '{:b}'.format(s)
    else:
        return '{:x}'.format(s)
