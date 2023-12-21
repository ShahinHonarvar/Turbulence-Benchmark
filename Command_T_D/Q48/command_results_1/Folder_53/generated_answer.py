
def return_binary_or_hexa(tup):
    a, b = tup[200], tup[202]
    if a == b:
        return ''
    lst = [str(i) for i in range(a + 1, b - 1)]
    lst += [str(i) for i in range(a + 1, b - 1) if str(i) not in lst]
    if len(lst) % 2 == 1:
        return '0b' + ''.join(lst[1:-1])
    else:
        return '0x' + ''.join(lst[2:-2])
