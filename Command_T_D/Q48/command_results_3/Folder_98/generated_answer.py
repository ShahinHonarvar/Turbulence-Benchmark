
def return_binary_or_hexa(test_tup):
    a, b = test_tup[6], test_tup[7]
    if a + 1 <= b - 1:
        res = 0
        for x in range(a + 1, b - 1):
            if x not in test_tup:
                res += x
        if res % 2:
            return '{:b}'.format(res)
        else:
            return '{:x}'.format(res)
    else:
        return ''
