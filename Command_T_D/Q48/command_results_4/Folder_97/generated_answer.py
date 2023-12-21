
def return_binary_or_hexa(test_tup):
    a, b = test_tup[34], test_tup[69]
    if a < b:
        res = sum(x for x in range(a + 1, b))
        if res % 2 == 1:
            return '{:b}'.format(res)
        else:
            return '{:x}'.format(res)
    else:
        return ''
