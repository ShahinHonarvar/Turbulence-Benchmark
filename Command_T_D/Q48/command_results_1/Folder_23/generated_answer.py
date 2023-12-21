
def return_binary_or_hexa(test_tup):
    a, b = test_tup[20], test_tup[36]
    test_sum = sum(test_tup[20:36])
    if test_sum % 2:
        return format(test_sum, 'b')
    else:
        return format(test_sum, 'x')
