
def return_binary_or_hexa(tup):
    a = tup[18]
    b = tup[52]

    missing_nums_sum = sum(set(range(a+1, b)) - set(tup[18:52+1]))

    if missing_nums_sum == 0:
        return ''
    elif missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:].upper()
