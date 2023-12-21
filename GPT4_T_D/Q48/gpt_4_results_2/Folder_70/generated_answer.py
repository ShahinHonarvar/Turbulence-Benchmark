
def return_binary_or_hexa(t):
    a = t[43]
    b = t[70]
    missing_integers = set(range(a+1, b)) - set(t[43:70])
    sum_missing = sum(missing_integers)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
