
def return_binary_or_hexa(t):
    a = t[0]
    b = t[10]
    s = set(range(a + 1, b))
    t_set = set(t[1:11])
    missing_nums = s - t_set
    if not missing_nums:
        return ""
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()
