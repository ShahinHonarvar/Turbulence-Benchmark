
def return_binary_or_hexa(tuple):
    a = tuple[70]
    b = tuple[98]
    missing_integers = set(range(a+1, b)) - set(tuple[70:98])
    summed_ints = sum(missing_integers)

    if summed_ints == 0:
        return ""
    elif summed_ints%2 == 0:
        return hex(summed_ints)[2:]
    else:
        return bin(summed_ints)[2:]
