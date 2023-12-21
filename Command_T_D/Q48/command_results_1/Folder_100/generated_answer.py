
def return_binary_or_hexa(tup):
    a, b = tup[44], tup[78]
    mid = (a + b) // 2
    sm = sum(range(a + 1, mid))
    if sm % 2 == 0:
        return hex(sm)
    else:
        return bin(sm)
