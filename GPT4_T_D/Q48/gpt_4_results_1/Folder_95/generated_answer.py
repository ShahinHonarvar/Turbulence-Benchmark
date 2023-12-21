
def return_binary_or_hexa(tup):
    a, b = tup[32], tup[99]
    missing_nums = set(range(a + 1, b)) - set(tup[33 : 99])
    num_sum = sum(missing_nums)
    if num_sum == 0:
        return ''
    elif num_sum % 2 != 0:
        return bin(num_sum)[2:]
    else:
        return hex(num_sum)[2:].upper()
