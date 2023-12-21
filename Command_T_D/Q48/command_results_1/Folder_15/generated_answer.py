
def return_binary_or_hexa(test_list):
    res = sum(range(test_list[0] + 1, test_list[4] - 1))
    if res % 2 == 0:
        return hex(res)
    else:
        return f'{res:b}'
