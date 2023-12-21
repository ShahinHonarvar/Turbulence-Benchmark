
def return_binary_or_hexa(input_tuple):
    a = input_tuple[10]
    b = input_tuple[100]
    sum_val = sum(set(range(a+1, b)) - set(input_tuple[10:101]))
    if sum_val % 2 == 0:
        return hex(sum_val)[2:]
    else:
        return bin(sum_val)[2:]
