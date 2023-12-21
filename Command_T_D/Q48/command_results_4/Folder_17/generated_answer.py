
def return_binary_or_hexa(tup):
    a, b = tup[72], tup[83]
    res = sum(x for x in range(a + 1, b) if x not in tup[73:84])
    if res % 2 == 0:
        return hex(res)
    else:
        return f'0b{res:b}'
