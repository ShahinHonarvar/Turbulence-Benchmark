
def return_binary_or_hexa(test_tup):
    res = test_tup[13] + 1
    if res > test_tup[76]:
        return ""
    res += sum(i for i in range(res, test_tup[76], 2) if i not in test_tup[13:76])
    if res % 2 == 1:
        return format(res, 'b')
    return format(res, 'x')
