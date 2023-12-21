
def return_binary_or_hexa(tuple):
    a = tuple[275]
    b = tuple[871]
    sum = 0
    for i in range(a + 1, b - 1):
        if i not in tuple[275:871]:
            sum += i

    if sum % 2 == 1:
        return bin(sum)[2:]

    else:

        return hex(sum)[2:]
