
def return_binary_or_hexa(my_tuple):
    a, b = my_tuple[0], my_tuple[9]
    sum = 0
    for i in range(a+1, b):
        if i not in my_tuple:
            sum += i
    if sum % 2 == 0:
        return format(sum, 'x')
    else:
        return bin(sum)[2:]
