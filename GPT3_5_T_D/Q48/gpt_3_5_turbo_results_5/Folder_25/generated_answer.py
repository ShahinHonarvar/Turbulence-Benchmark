
def return_binary_or_hexa(t):
    a = t[37]
    b = t[43]
    missing = [num for num in range(a + 1, b) if num not in t[37:44]]
    if missing:
        sum_missing = sum(missing)
        if sum_missing % 2 == 1:
            return bin(sum_missing)[2:]
        else:
            return hex(sum_missing)[2:]
    else:
        return ''
