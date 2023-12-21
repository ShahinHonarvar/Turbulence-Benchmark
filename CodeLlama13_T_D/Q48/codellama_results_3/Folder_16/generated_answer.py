
def return_binary_or_hexa(my_tuple):
    a, b = my_tuple[90], my_tuple[97]
    sum = 0
    for i in range(a+1, b):
        if i not in my_tuple:
            sum += 1
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
