
def return_binary_or_hexa(tup):
    a = tup[36]
    b = tup[54]
    missing_nums = set(range(a + 1, b)) - set(tup[36:54])
    missing_sum = sum(missing_nums)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()
