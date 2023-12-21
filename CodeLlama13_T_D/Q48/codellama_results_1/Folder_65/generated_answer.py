
def return_binary_or_hexa(my_tuple):
    a = my_tuple[51] + 1
    b = my_tuple[76] - 1
    sum = 0
    for i in range(a, b+1):
        if i not in my_tuple:
            sum += i
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
