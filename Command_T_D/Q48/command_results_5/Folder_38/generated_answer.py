
def return_binary_or_hexa(test_tup):
    a, b = sorted(test_tup)[36], sorted(test_tup)[85]
    if a + 1 <= b - 1:
        val = sum(x for x in range(a + 1, b - 1) if x not in test_tup)
        if val % 2 == 1:
            return format(val, 'b')
        return format(val, 'x')
    return ''
