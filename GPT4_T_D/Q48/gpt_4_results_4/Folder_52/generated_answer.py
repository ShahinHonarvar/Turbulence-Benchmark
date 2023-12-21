
def return_binary_or_hexa(tuple_input):
    a = tuple_input[38]
    b = tuple_input[81]
    
    num_sum = sum(set(range(a+1, b)) - set(tuple_input[38:82]))
    
    if num_sum == 0:
        return ""
    
    if num_sum % 2 == 0:
        return hex(num_sum)[2:]
    else:
        return bin(num_sum)[2:]
