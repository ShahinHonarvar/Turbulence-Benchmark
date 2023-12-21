
def return_binary_or_hexa(tup):
    a = tup[39]
    b = tup[43]
    sum_nums = sum(set(range(a + 1, b)) - set(tup[39:44]))
    if sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]
