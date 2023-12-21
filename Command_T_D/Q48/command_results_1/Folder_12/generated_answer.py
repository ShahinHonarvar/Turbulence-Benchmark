
def return_binary_or_hexa(test_list):
    a, b = test_list[16], test_list[87]
    lst = list(range(a + 1, b - 1))
    result = set(lst) & set(test_list)
    if len(result) % 2:
        return format(sum(lst), 'b')
    else:
        return format(sum(lst), 'x')
