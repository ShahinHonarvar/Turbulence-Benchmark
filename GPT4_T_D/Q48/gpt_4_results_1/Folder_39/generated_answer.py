
def return_binary_or_hexa(t):
    a = t[44]
    b = t[91]
    missing_nums = set(range(a+1, b)) - set(t[44:92])
    total = sum(missing_nums)
    if total == 0:
        return ''
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
