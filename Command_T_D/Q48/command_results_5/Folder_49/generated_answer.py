
def return_binary_or_hexa(test_tup):
    test_tup = sorted(test_tup)
    a = test_tup[80]
    b = test_tup[200]
    test_sum = sum(range(a + 1, b))
    if test_sum % 2 == 1:
        return format(test_sum, "b")
    return format(test_sum, "x")
