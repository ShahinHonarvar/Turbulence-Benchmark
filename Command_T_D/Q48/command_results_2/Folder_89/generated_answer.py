
def return_binary_or_hexa(tup):
    a, b = tup[55], tup[84]
    if a <= b:
        return str(a + 1)
    else:
        return str(a + 1) + b - a - 1
