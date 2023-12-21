
def return_binary_or_hexa(my_tuple):
    a = my_tuple[44]
    b = my_tuple[78]
    sum = 0
    for i in range(a + 1, b):
        if i not in my_tuple:
            sum += i

    if sum % 2 == 0:
        return hex(sum).upper().replace("0X", "")

    else:

        return bin(sum).replace("0b", "")
