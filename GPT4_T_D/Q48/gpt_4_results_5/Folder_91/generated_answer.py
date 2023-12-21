
def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[6]
    total = sum(num for num in range(a + 1, b) if num not in tup[1:7])
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
    return ""
