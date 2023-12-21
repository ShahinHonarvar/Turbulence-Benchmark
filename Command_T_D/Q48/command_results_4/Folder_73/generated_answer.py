
def return_binary_or_hexa(test_list):
    a, b = test_list[10], test_list[76]
    if sum(x for x in range(a + 1, b)) % 2:
        return format(sum(x for x in range(a + 1, b)), 'b')
    else:
        return format(sum(x for x in range(a + 1, b)), 'x')
