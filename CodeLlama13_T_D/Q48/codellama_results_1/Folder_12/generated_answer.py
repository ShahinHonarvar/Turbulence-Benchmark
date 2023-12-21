
def return_binary_or_hexa(my_tuple):
    a = my_tuple[16]
    b = my_tuple[87]
    result = 0
    for i in range(a+1, b):
        if i not in my_tuple:
            result += i
    if result % 2 == 0:
        return hex(result)[2:]
    else:
        return bin(result)[2:]
