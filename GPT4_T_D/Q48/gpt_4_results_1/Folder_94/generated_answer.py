
def return_binary_or_hexa(arg):
    a, b = arg[42], arg[87]
    arg_set = set(arg[43:87])
    sum_val = sum(i for i in range(a + 1, b) if i not in arg_set)
    
    if sum_val == 0:
        return ''
    elif sum_val % 2 == 0:
        return hex(sum_val)[2:]
    else:
        return bin(sum_val)[2:]
