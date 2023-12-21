
def return_binary_or_hexa(tup):
    s = sum(x for x in range(tup[0] + 1, tup[2] - 1) if x not in tup)
    return str(s).zfill(len(str(s))) if s else ''
