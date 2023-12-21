
def return_binary_or_hexa(t):
    a = t[10]
    b = t[100]
    total = 0
    elements = set(t[10:101])
    for i in range(a+1, b):
        if i not in elements:
            total += i
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
