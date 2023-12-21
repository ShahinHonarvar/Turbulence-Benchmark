
def return_binary_or_hexa(tuple):
    a = tuple[20]
    b = tuple[51]
    sum = 0


    for i in range(a + 1, b - 1):
        if not i in tuple[20:51]:
            sum += i


    if sum % 2 == 0:
        return hex(sum)


    else:

        return bin(sum)
