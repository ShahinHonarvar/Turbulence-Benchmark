
def return_binary_or_hexa(t):
    a = t[1]
    b = t[4]
    missing_nums_sum = sum([i for i in range(a + 1, b) if i not in t[1:5]])
    if missing_nums_sum == 0:
        return ''
    elif missing_nums_sum % 2 == 0:
        return str(hex(missing_nums_sum))[2:].upper()
    else:
        return str(bin(missing_nums_sum))[2:]
