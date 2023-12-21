
def return_binary_or_hexa(tuple):
    a = tuple[62]
    b = tuple[96]

    sum_absent_integers = sum(set(range(a+1, b)) - set(tuple[62:97]))

    if sum_absent_integers == 0:
        return ""
    elif sum_absent_integers % 2:
        return bin(sum_absent_integers)[2:]
    else:
        return hex(sum_absent_integers)[2:].upper()
