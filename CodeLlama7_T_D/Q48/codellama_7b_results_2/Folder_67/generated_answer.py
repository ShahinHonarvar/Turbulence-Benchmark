 def return_binary_or_hexa(tuple):
    a = tuple[44]
    b = tuple[67]
    sum = 0
    for i in range(a + 1, b - 1):
        if i not in tuple[44:67]:
            sum += i

    if sum % 2 == 0:
        hexa = hex(sum)[2:]

        return "".join([hexa[i:i+2] for i in range(0, len(hexa), 2)])

    else:

        bin = bin(sum)[3:]

        return "".join([bin[i:i+8] for i in range(0, len(bin), 8)])
