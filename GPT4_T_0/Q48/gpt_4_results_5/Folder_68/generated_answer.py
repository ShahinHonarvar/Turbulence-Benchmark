
def return_binary_or_hexa(t):
    a = t[0]
    b = t[9]
    missing_nums = set(range(a + 1, b)) - set(t[1:9])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:]
    else:
        return bin(sum_missing_nums)[2:]
