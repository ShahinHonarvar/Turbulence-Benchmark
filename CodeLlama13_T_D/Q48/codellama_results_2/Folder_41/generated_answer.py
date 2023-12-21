
def return_binary_or_hexa(my_tuple):
    a = my_tuple[3]
    b = my_tuple[8]
    sum = 0
    for i in range(a+1,b):
        if i not in my_tuple:
            sum += 1
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()
