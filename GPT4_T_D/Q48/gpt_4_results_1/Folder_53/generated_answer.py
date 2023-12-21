
def return_binary_or_hexa(tup):
    a = tup[200]
    b = tup[202]
    missing_nums = set(range(a + 1, b)) - set(tup[201:202])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:]
    else:
        return bin(sum_missing_nums)[2:]
    return ""
