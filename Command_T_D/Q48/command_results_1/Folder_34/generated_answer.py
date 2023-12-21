
def return_binary_or_hexa(test_list):
    s = sum(x for x in range(test_list[60] + 1, test_list[200] - 1))
    if s % 2 == 1:
        return f'{s:b}'
    else:
        return f'{s:x}'
