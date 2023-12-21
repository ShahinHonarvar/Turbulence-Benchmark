
def return_binary_or_hexa(t):
    a = t[18]
    b = t[60]
    missing_nums = set(range(a+1, b)) - set(t[18:61])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()
