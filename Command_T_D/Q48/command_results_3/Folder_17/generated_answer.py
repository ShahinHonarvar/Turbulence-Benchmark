
def return_binary_or_hexa(tup):
    a, b = tup[73], tup[84]
    lst = range(a + 1, b - 1)
    if set(lst).issubset(tup):
        return ""
    return hex(sum(lst)) if sum(lst) % 2 == 0 else "0b{}".format(bin(sum(lst)))
