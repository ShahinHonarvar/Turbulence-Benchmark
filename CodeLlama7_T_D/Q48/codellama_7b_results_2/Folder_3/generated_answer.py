 def return_binary_or_hexa(tuple):
    a = tuple[56]
    b = tuple[88]
    sum = 0


    for i in range(a + 1, b):
        if not i in tuple[56:88]:
            sum += i


    if sum % 2 == 1:
        return bin(sum)[2:]


    else:
        return hex(sum)[2:]
