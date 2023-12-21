
def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[35]
    s = set(tup[13:36])
    sum_nums = sum(set(range(a+1, b)) - s)
    if sum_nums == 0:
        return ''
    elif sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:].upper()
