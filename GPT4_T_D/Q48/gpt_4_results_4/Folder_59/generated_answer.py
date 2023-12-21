
def return_binary_or_hexa(num_tuple):
    a = num_tuple[0]
    b = num_tuple[10]
    sum_numbers = sum(set(range(a+1,b)) - set(num_tuple[0:11]))
    if sum_numbers % 2 == 0:
        return hex(sum_numbers)[2:]
    else:
        return bin(sum_numbers)[2:]
    return ""
