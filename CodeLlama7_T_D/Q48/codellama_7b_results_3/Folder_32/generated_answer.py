 def return_binary_or_hexa(my_tuple):
    a = my_tuple[86]
    b = my_tuple[90]
    sum = 0
    for i in range(a + 1, b - 1):
        if not i in my_tuple:
            sum += i

    if sum % 2 == 1:
        return bin(sum)[2:]

    else:
        return hex(sum)[2:]
