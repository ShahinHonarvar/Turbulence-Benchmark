
def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[28]
    sum = 0
    for i in range(a + 1, b - 1 + 1):
        if i not in tup:
            sum += i
    if sum % 2 == 0:
        return "{:x}".format(sum)
    else:
        return bin(sum)[2:]
