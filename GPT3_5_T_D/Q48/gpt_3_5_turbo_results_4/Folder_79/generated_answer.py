
def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[7]
    total = 0
    for i in range(a + 1, b):
        if i not in tup[1:7]:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
