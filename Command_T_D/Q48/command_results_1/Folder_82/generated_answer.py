
def return_binary_or_hexa(tup):
    res = sum(
        x
        for x in range(tup[20] + 1, tup[200] - 1)
        if x not in tup[20:200]
    )
    if res % 2 == 0:
        return hex(res)
    else:
        return bin(res)
