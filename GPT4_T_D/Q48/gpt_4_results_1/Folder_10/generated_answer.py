
def return_binary_or_hexa(tup):
    a = tup[36]
    b = tup[54]

    sum_missing = sum(range(a+1, b)) - sum(tup[37:54])
    
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()
