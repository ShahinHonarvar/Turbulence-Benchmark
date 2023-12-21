
def return_binary_or_hexa(tup):
    a, b = tup[50], tup[92]
    return ("".join(str(x) for x in range(a + 1, b - 1) if x not in tup),
