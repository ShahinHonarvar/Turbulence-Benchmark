
def return_binary_or_hexa(tup):
    a, b = tup[57], tup[84]
    lst = list(range(a + 1, b - 1))
    for x in range(a + 1, b - 1):
        if x not in tup:
            break
    if len(lst) == 0:
        return ''
    if len(lst) % 2 == 1:
        return '0b' + bin(sum(lst)).zfill(len(lst)).decode('utf-8')
    return '0x' + hex(sum(lst)).zfill(len(lst)).decode('utf-8')
