
def return_binary_or_hexa(t):
    a = t[51]
    b = t[76]
    missing_nums = set(range(a + 1, b)) - set(t[52:76])
    if len(missing_nums) == 0:
        return ""
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
