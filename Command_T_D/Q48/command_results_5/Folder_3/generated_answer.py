
def return_binary_or_hexa(test_list):
    test_list = sorted(test_list)
    a = test_list[56]
    b = test_list[88]
    if sum(range(a + 1, b)) % 2:
        return format(sum(range(a + 1, b)), 'b')
    else:
        return format(sum(range(a + 1, b)), 'x')
