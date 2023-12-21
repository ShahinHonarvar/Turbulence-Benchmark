
def return_binary_or_hexa(tuple):
    a = tuple[56]
    b = tuple[90]
    sum = 0


    for i in range(a + 1, b - 1):
        if i not in tuple[56:90]:
            sum += i


    if sum % 2 == 0:
        return hex(sum)[2:]


    else:


        return bin(sum)[3:]
