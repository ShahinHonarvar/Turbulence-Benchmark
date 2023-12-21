
def return_binary_or_hexa(t):
    a = t[0]
    b = t[9]
    total = 0
    for i in range(a + 1, b):
        if i not in t[1:9]:
            total += i

    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
