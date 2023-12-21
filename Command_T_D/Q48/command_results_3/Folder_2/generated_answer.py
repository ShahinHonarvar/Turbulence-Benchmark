
def return_binary_or_hexa(tup):
    a, b = tup[72], tup[93]
    sm = sum(tup[a:b])
    if sm % 2:
        return format(sm, 'b')
    return format(sm, 'x')
