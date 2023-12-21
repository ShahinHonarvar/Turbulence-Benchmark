
def return_binary_or_hexa(t):
    a, b = t[0], t[8]
    missing_nums = set(range(a + 1, b)) - set(t[1:8])
    num_sum = sum(missing_nums)
    if num_sum == 0:
        return ''
    elif num_sum % 2 == 1:
        return bin(num_sum)[2:]
    else:
        return hex(num_sum)[2:].upper()
