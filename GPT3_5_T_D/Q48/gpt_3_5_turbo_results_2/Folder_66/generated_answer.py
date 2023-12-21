
def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[11]
    b = tuple_of_integers[76]
    range_sum = 0
    
    for i in range(a+1, b):
        if i not in tuple_of_integers[12:76]:
            range_sum += i
    
    if range_sum % 2 == 0:
        return hex(range_sum)[2:]
    else:
        return bin(range_sum)[2:]
