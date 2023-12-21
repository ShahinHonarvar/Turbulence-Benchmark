
def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[43]
    missing_nums = set(range(a + 1, b)) - set(tup[20:44])
    total_sum = sum(missing_nums)
    if total_sum == 0:
        return ""
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
