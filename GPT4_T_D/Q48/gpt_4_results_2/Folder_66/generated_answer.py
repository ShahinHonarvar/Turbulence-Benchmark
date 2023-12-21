
def return_binary_or_hexa(tup):
    a, b = tup[11], tup[76]
    missing_nums = set(range(a + 1, b)) - set(tup[11:77])
    sum_nums = sum(missing_nums)
    if sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:]
