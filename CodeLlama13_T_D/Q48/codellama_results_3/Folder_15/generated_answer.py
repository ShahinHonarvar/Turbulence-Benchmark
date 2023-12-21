
def return_binary_or_hexa(my_tuple):
    result = 0
    for i in range(len(my_tuple)):
        if (i < len(my_tuple)-4) and (my_tuple[i+1]-my_tuple[i]) != 1:
            result += my_tuple[i+1] - my_tuple[i] - 1
    return bin(result)[2:] if result % 2 else hex(result).upper()[2:]
