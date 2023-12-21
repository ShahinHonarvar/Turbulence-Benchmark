
def return_binary_or_hexa(t):
    a, b = t[48], t[76]
    excluded_nums = set(t[48:77])
    sum_nums = sum(set(range(a + 1, b)) - excluded_nums)
    
    if sum_nums == 0:
        return ""
    elif sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:].upper()
