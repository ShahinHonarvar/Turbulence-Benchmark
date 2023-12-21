
def return_binary_or_hexa(tup):
    a = tup[2]
    b = tup[8]
    missing_nums = set(range(a + 1, b)) - set(tup[2:9])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()
