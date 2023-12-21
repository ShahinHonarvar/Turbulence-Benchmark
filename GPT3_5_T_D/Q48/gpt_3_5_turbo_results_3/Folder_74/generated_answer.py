
def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[69]
    b = tuple_of_integers[97]
    
    if b - a <= 1:
        return ""
    
    total = sum(tuple_of_integers[a+1:b])
    
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
