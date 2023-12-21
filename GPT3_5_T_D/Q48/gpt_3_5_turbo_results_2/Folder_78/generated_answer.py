
def return_binary_or_hexa(t):
    a = t[62]
    b = t[96]
    total = 0
    for i in range(a+1, b):
        if i not in t[62:97]:
            total += i
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]
