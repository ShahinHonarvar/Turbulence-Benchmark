
def return_binary_or_hexa(my_tuple):
    a = my_tuple[10]
    b = my_tuple[100]
    sum = 0
    for i in range(a + 1, b - 1 + 1):
        if i not in my_tuple[10:100]:
            sum += i

    if sum % 2 != 0:

        return bin(sum)[2:]

    else:

        return hex(sum)[2:]
