
def return_binary_or_hexa(test_list):
    a, b = test_list[55], test_list[84]
    test_sum = sum(test_list[a + 1 : b])
    if test_sum % 2:
        return format(test_sum, "b")
    else:
        return format(test_sum, "x")
