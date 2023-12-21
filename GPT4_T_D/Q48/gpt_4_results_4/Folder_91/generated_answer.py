
def return_binary_or_hexa(num_tuple):
    a = num_tuple[0]
    b = num_tuple[6]
    missing_nums_sum = sum(set(range(a+1,b)) - set(num_tuple[1:7]))
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:].upper()
