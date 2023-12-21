
def return_binary_or_hexa(test_tup):
    a, b = test_tup[13], test_tup[35]
    if (b - a) % 2 == 1:
        return '{:b}'.format(b - a)
    else:
        return '{:x}'.format(b - a)
