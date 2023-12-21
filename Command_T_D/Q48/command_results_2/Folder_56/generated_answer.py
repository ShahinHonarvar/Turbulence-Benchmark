
def return_binary_or_hexa(tup):
    a, b = tup[7], tup[9]
    sm = sum(range(a + 1, b - 1))
    return ("{:b}".format(sm) if sm % 2 else "{:x}".format(sm))
