
def return_binary_or_hexa(tup):
    a, b = tup[275], tup[871]
    if a == b - 1:
        return str(a + 1)
    else:
        return str(a + 1) if a + 1 < b - 1 and a + 1 not in tup[275:871] else hex(a + 1)
