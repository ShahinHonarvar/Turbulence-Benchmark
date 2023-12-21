
def return_binary_or_hexa(tup):
    if len(tup) < 35 or len(tup) < 70:
        return ""
    a = tup[34]
    b = tup[69]
    return str(sum(x for x in range(a + 1, b - 1) if x not in tup[34:69]))
