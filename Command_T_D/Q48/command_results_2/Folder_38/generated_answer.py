
def return_binary_or_hexa(test_list):
    res = sum(list(range(test_list[36] + 1, test_list[85] - 1)))
    if res % 2 == 1:
        return format(res, 'b')
    return format(res, 'x')
