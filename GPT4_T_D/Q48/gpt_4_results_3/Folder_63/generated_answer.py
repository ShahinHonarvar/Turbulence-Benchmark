
def return_binary_or_hexa(t):
    a, b = t[81], t[86]
    missing_integers = set(range(a+1, b)) - set(t[82:86])
    sum_of_missing = sum(missing_integers)

    if sum_of_missing == 0:
        return ''
    elif sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]
