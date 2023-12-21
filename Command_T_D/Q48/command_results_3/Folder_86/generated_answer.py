
def return_binary_or_hexa(test_list):
    odd = True
    a = test_list[19]
    b = test_list[32]
    for i in range(a + 1, b - 1):
        if i not in test_list:
            odd = False
            break
    if odd:
        return format(sum(list(range(a + 1, b - 1))), 'b')
    else:
        return format(sum(list(range(a + 1, b - 1))), 'x')
