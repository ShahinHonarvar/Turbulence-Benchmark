
def return_binary_or_hexa(tup):
    a = tup[275]
    b = tup[871]
    missing_integers_sum = sum(set(range(a+1, b)) - set(tup[275:872]))

    if missing_integers_sum == 0:
        return ""
    elif missing_integers_sum % 2 == 1:
        return bin(missing_integers_sum)[2:]
    else:
        return hex(missing_integers_sum)[2:].upper()
