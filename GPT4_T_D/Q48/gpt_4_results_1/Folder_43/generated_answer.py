
def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[28]
    
    missing_integers = set(range(a + 1, b)) - set(tup[11:28])
    sum_missing_integers = sum(missing_integers)
    
    if sum_missing_integers == 0:
        return ''
    elif sum_missing_integers % 2 == 0:
        return hex(sum_missing_integers)[2:]
    else:
        return bin(sum_missing_integers)[2:]
