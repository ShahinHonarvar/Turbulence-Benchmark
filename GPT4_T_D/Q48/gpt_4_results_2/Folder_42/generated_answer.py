
def return_binary_or_hexa(tup):
    a = tup[18]
    b = tup[60]
    missing_nums = set(range(a+1, b)) - set(tup[19:60])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 != 0:
        return bin(sum_missing_nums)[2:]
    elif sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:].upper()
    else:
        return ''
