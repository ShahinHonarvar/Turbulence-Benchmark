
def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[27]
    b = tuple_of_integers[96]
    missing = set(range(a + 1, b)) - set(tuple_of_integers[27:97])
    sum_missing = sum(missing)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
