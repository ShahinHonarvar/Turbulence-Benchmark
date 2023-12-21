
def return_binary_or_hexa(test_tup):
    a, b = test_tup[11], test_tup[76]
    res = sum(range(a + 1, b)) % 2
    return ("{:b}".format(res), "{:x}".format(res))
