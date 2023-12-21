
def return_binary_or_hexa(test_tup):
    a, b = test_tup[22], test_tup[24]
    if a == b:
        return ""
    if a % 2 == 1:
        return format(sum(test_tup[a:b]), 'b')
    else:
        return format(sum(test_tup[a:b]), 'x')
