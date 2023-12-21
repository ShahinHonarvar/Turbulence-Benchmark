
def return_binary_or_hexa(num_tuple):
    a = num_tuple[50]
    b = num_tuple[92]
    sum_values = sum(set(range(a+1, b)) - set(num_tuple[50:93]))
    if sum_values == 0:
        return ""
    elif sum_values % 2 == 0:
        return hex(sum_values)[2:]
    else:
        return bin(sum_values)[2:]
