
def return_binary_or_hexa(test_tup):
    a, b = test_tup[18], test_tup[60]
    diff = b - a - 1
    if diff % 2 == 1:
        return format(diff, 'b')
    else:
        return format(diff, 'x')
