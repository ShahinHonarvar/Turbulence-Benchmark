
def return_binary_or_hexa(tpl):
    a = tpl[1]
    b = tpl[7]
    missing_nums = set(range(a + 1, b)) - set(tpl[1:8])
    summation = sum(missing_nums)
    if summation == 0:
        return ""
    elif summation % 2 == 0:
        return hex(summation)[2:]
    else:
        return bin(summation)[2:]
