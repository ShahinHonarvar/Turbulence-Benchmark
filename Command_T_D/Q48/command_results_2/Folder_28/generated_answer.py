
def return_binary_or_hexa(test_tup):
    a, b = test_tup[86], test_tup[99]
    test_s = str(sum(x for x in range(a + 1, b - 1) if x not in test_tup))
    if test_s % 2:
        return test_s
    else:
        return hex(int(test_s))
