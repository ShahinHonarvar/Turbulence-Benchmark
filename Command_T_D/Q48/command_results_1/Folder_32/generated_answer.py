
def return_binary_or_hexa(tup):
    a, b = tup[86], tup[90]
    sum1 = sum(x for x in range(a + 1, b))
    if sum1 % 2 == 1:
        return bin(sum1).zfill(len(bin(sum1))).rstrip("0b")
    else:
        return hex(sum1).zfill(len(hex(sum1))).rstrip("0x")
