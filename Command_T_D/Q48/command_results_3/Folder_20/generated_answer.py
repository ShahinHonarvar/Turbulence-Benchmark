
def return_binary_or_hexa(test_list):
    a, b = 27, 96
    test_sum = sum(x for x in range(a + 1, b - 1) if x not in test_list)
    if test_sum % 2 == 0:
        return hex(test_sum)
    else:
        return f'{test_sum:b}'
