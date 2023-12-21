
def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[67]
    missing_numbers_sum = sum(set(range(a+1, b)) - set(tup[44:68]))
    if missing_numbers_sum == 0:
        return ''
    elif missing_numbers_sum % 2 == 0:
        return hex(missing_numbers_sum)[2:].upper()
    else:
        return bin(missing_numbers_sum)[2:]
