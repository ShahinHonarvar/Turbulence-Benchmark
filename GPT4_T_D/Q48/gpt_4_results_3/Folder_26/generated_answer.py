
def return_binary_or_hexa(tup):
    a = tup[68]
    b = tup[99]
    missing_nums = set(range(a+1, b)) - set(tup[68:99])
    sum_nums = sum(missing_nums)
    if sum_nums == 0:
        return ""
    elif sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]
