
def return_binary_or_hexa(tup):
    a = tup[27] + 1
    b = tup[96] - 1
    sum = 0
    for i in range(a, b+1):
        if i not in tup:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
