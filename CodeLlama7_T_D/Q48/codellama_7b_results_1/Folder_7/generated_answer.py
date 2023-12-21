
def return_binary_or_hexa(my_tuple):
    a = my_tuple[10]
    b = my_tuple[97]
    sum = 0
    for i in range(a + 1, b - 1):
        if i not in my_tuple:
            sum += i

    if sum % 2 == 0:
        return "{:x}".format(sum)

    else:
        return "{:b}".format(sum)
