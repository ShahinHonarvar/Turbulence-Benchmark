
def return_binary_or_hexa(tup):
    a, b = tup[44], tup[91]
    if (b - a - 1) % 2:
        return bin(a + 1 + b - 1).zfill(a + b - 1)
    else:
        return hex(a + 1 + b - 1).zfill(a + b - 1)
