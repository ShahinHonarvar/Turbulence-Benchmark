
def return_binary_or_hexa(my_tuple):
    a = my_tuple[73]
    b = my_tuple[84]
    sum = 0
    for i in range(a + 1, b - 1):
        if i not in my_tuple[73:85]:
            sum += i

    if sum % 2 == 0:
        return hex(sum)[2:]

    else:

        return bin(sum)[3:]
