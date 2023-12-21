
def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[76]
    sum_nums = sum(set(range(a + 1, b)) - set(tup[11:76]))
    if sum_nums % 2 == 0:
        return format(sum_nums, 'x')
    else:
        return format(sum_nums, 'b')
