
def return_binary_or_hexa(my_tuple):
    a = my_tuple[20]
    b = my_tuple[36]
    sum = 0
    for i in range(a + 1, b - 1 + 1):
        if not i in my_tuple:
            sum += i

    if sum % 2 == 1:
        return "{}".format(sum)

    else:

        return "{:x}".format(sum)
