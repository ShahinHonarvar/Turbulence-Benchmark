
def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[86]
    b = tuple_of_integers[90]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple_of_integers[87:90]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
