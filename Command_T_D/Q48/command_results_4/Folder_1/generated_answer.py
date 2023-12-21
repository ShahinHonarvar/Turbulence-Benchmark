
def return_binary_or_hexa(tup):
    a, b = tup[17], tup[88]
    a += 1
    b -= 1
    str1 = "0" * (a.bit_length() - 1)
    for x in range(a, b + 1):
        if x not in tup[17:88]:
            str1 += "1"
    if len(str1) % 2 == 0:
        return hex(int(str1))
    return str1
