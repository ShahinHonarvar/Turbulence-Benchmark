
def return_binary_or_hexa(tup):
    a, b = sorted(tup)[0] + 1, sorted(tup)[8] - 1
    val = b - a - sum(1 for i in range(a, b) if i in tup)
    return str(val) if val % 2 else hex(val)
