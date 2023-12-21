
def return_binary_or_hexa(test_list):
    test_list = list(test_list)
    test_list.sort()
    a = test_list[0]
    b = test_list[8]
    test_list.sort()
    list_num = b - a - 1
    if list_num % 2 == 1:
        return format(list_num, 'b')
    else:
        return format(list_num, 'x')
