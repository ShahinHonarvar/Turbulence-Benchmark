
def return_binary_or_hexa(num_tuple):
    a = num_tuple[20]
    b = num_tuple[36]
    num_range = set(range(a + 1, b))
    num_present = set(num_tuple[21:36])
    
    num_not_present = num_range - num_present
    
    if len(num_not_present) == 0:
        return ""
    
    sum_num = sum(num_not_present)
    
    if sum_num % 2 == 0:
        return hex(sum_num)[2:]
    else:
        return bin(sum_num)[2:]
