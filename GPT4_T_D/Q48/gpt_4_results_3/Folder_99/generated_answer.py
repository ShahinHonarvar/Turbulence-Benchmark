
def return_binary_or_hexa(arg):
    a, b = arg[427], arg[669]
    missing_elems = set(range(a+1, b)) - set(arg[427:670])
    sum_val = sum(missing_elems)
    
    if not missing_elems:
        return ''
    elif sum_val % 2 == 0:
        return hex(sum_val)[2:]
    else:
        return bin(sum_val)[2:]
