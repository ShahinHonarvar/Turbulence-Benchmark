
def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[76]
    sum = 0
    for i in range(a+1, b-1):
        if i not in tup:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum).upper()[2:]
