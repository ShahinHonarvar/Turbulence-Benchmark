
def return_binary_or_hexa(t):
    a, b = t[3], t[9]
    missing_nums = set(range(a + 1, b)) - set(t[3:10])
    sum_nums = sum(missing_nums)
    if not missing_nums:
        return ''
    else:
        if sum_nums % 2:
            return bin(sum_nums)[2:]
        else:
            return hex(sum_nums)[2:].upper()
