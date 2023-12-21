
def return_binary_or_hexa(tup):
    a, b = tup[13], tup[76]
    sum_val = sum(i for i in range(a+1, b) if i not in tup[13:77])
    if sum_val == 0:
        return ''
    elif sum_val % 2 == 0:
        return hex(sum_val)[2:].upper()
    else:
        return bin(sum_val)[2:]
