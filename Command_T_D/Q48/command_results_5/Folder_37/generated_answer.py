
def return_binary_or_hexa(tup):
    a, b = tup[2], tup[7]
    if a == b:
        return ''
    sum_ = sum(n for n in range(a + 1, b - 1))
    if sum_ % 2 == 1:
        return '{:b}'.format(sum_)
    return '{:x}'.format(sum_)
