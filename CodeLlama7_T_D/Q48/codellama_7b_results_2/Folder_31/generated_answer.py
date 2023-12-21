 def return_binary_or_hexa(tuple):
    a = tuple[33]
    b = tuple[78]
    sum = 0

    for i in range(a + 1, b - 1 + 1):
        if i not in tuple[33:78 + 1]:
            sum += i

    if sum % 2 == 1:
        return '{}{}'.format('' if len(bin(sum)) > 3 else '0b', bin(sum)[2:])
    else:
        return '{}{}'.format('' if len(hex(sum)) > 3 else '0x', hex(sum)[2:].upper())
