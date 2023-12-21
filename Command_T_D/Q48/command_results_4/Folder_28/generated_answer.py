
def return_binary_or_hexa(tup):
    a, b = tup[86], tup[99]
    n = b - a - 1
    if n % 2 == 1:
        return format(n, 'b')
    else:
        return format(n, 'x')
