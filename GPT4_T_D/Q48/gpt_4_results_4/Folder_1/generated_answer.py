
def return_binary_or_hexa(tup):
    a = tup[17]
    b = tup[88]
    missing_nums = set(range(a+1,b)) - set(tup[17:89])
    total_sum = sum(missing_nums)
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
