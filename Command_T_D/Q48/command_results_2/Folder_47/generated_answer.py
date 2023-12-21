
def return_binary_or_hexa(test_tup):
    a, b = sorted(test_tup)[29], sorted(test_tup)[53]
    s = sum(x for x in range(a + 1, b - 1) if x not in test_tup[29:53])
    if s % 2:
        return '{:b}'.format(s)
    else:
        return '{:x}'.format(s)
