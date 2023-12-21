
def return_binary_or_hexa(tup):
    a = tup[36]
    b = tup[85]
    missing_nums = set(range(a + 1, b)) - set(tup[36:86])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()
