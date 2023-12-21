
def return_binary_or_hexa(tup):
    a, b = tup[44], tup[67]
    sum1 = b - a - 1
    if sum1 % 2 == 0:
        return hex(sum1)
    else:
        return bin(sum1)
