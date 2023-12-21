
def return_binary_or_hexa(t):
    a, b = t[68], t[99]
    absent_nums = set(range(a + 1, b)) - set(t[68:99])
    sum_absent_nums = sum(absent_nums)
    if not absent_nums:
        return ""
    elif sum_absent_nums % 2 == 1:
        return bin(sum_absent_nums)[2:]
    else:
        return hex(sum_absent_nums)[2:]
