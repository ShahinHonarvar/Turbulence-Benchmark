
def return_binary_or_hexa(tup):
    res = 0
    for i in range(19, 32):
        if tup[i] not in tup[19:32]:
            res += tup[i]
    if res % 2 == 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:]
