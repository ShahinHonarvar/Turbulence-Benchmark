
def return_binary_or_hexa(tup):
    a, b = tup[37], tup[43]
    sm = sum(
        x for x in range(a + 1, b - 1) if x not in tup[37:-3] + tup[43:-1]
    )
    return str(sm).zfill(8) if not sm & 1 else hex(sm).zfill(8)
