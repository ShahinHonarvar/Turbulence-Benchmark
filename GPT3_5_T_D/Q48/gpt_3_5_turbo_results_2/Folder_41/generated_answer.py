
def return_binary_or_hexa(t):
    a = t[3]
    b = t[8]

    total = 0
    for i in range(a + 1, b):
        if i not in t[4:8]:
            total += i

    if total == 0:
        return ""
    elif total % 2 != 0:
        return "{0:b}".format(total)
    else:
        return "{0:X}".format(total)
