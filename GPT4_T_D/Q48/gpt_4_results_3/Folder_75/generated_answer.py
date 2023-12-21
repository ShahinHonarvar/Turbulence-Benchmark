
def return_binary_or_hexa(tup):
    if len(tup) < 52:
        return ""
    a, b = tup[20], tup[51]
    int_sum = sum(set(range(a + 1, b)) - set(tup[21:51]))
    if int_sum % 2 == 0:
        return format(int_sum, 'x')
    else:
        return format(int_sum, 'b')
