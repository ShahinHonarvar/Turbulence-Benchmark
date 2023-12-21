
def return_binary_or_hexa(my_tuple):
    a = my_tuple[20] + 1
    b = my_tuple[43] - 1
    sum = 0
    for i in range(a, b+1):
        if i not in my_tuple:
            sum += 1
    if sum % 2 == 0:
        return "{:x}".format(sum)
    else:
        return bin(sum)[2:]
