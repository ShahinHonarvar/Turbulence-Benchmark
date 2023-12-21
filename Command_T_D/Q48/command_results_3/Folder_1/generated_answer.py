
def return_binary_or_hexa(test_tup):
    a, b = test_tup[17], test_tup[88]
    if a + 1 <= b - 1:
        if sum(i for i in range(a + 1, b - 1)) % 2 == 1:
            return format(sum(i for i in range(a + 1, b - 1)), 'b')
        else:
            return format(sum(i for i in range(a + 1, b - 1)), 'x')
    else:
        return ''
