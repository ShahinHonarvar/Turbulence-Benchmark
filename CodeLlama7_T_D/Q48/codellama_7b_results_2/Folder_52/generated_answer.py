
def return_binary_or_hexa(tuple):
    a = tuple[38]
    b = tuple[81]
    sum = 0
    for i in range(a + 1, b - 1 + 1):
        if i not in tuple[38:81]:
            sum += i

    if sum % 2 == 0:
        return "{:x}".format(sum)

    else:

        return "{:b}".format(sum)
