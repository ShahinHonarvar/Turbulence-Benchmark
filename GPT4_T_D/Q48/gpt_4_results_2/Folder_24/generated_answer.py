
def return_binary_or_hexa(t):
    a = t[13]
    b = t[91]
    missing_nums = set(range(a + 1, b)) - set(t[13:92])
    num_sum = sum(missing_nums)
    if num_sum == 0:
        return ''
    elif num_sum % 2 == 0:
        return hex(num_sum)[2:]
    else:
        return bin(num_sum)[2:]
