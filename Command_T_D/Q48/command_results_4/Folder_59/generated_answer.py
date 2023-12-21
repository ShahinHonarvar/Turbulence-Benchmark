
def return_binary_or_hexa(test_tup):
    test_a, test_b = test_tup[0], test_tup[10]
    test_s = sum(i for i in range(test_a + 1, test_b - 1) if i not in test_tup[0:10])
    if test_s % 2 == 1:
        return '{:b}'.format(test_s)
    return '{:x}'.format(test_s)
