
def return_binary_or_hexa(num_tuple):
    a = num_tuple[20]
    b = num_tuple[200]
    sum_val = 0
    for i in range(a + 1, b):
        if i not in num_tuple[21:200]:
            sum_val += i
    if sum_val == 0:
        return ''
    elif sum_val % 2 == 0:
        return hex(sum_val)[2:]
    else:
        return bin(sum_val)[2:]
