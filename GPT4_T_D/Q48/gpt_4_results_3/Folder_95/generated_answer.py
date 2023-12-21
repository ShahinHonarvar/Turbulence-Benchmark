
def return_binary_or_hexa(t):
    a = t[32]
    b = t[99]
    missing_nums = set(range(a+1, b)) - set(t[32:100])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:]
