
def return_binary_or_hexa(test_list):
    test_list = sorted(set(test_list))
    test_list = list(range(test_list[10] + 1, test_list[79] - 1))
    test_list.sort()
    test_list = set(test_list)
    if test_list:
        if len(test_list) % 2 == 1:
            return format(sum(test_list) + 1, 'b')
        else:
            return format(sum(test_list) + 1, 'x')
    else:
        return ""
