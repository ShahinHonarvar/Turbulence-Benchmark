
def return_binary_or_hexa(tup):
    a = tup[7]
    b = tup[9]
    missing_nums = set(range(a + 1, b)) - set(tup[7:10])
    num_sum = sum(missing_nums)
    if num_sum == 0:
        return ''
    elif num_sum % 2 == 0:
        return hex(num_sum)[2:]
    else:
        return bin(num_sum)[2:]
