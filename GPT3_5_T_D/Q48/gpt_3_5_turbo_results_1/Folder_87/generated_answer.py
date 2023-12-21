
def return_binary_or_hexa(num_tuple):
    a = num_tuple[20]
    b = num_tuple[43]
    unique_nums = set(num_tuple[21:43])
    result = 0
    for num in range(a+1, b):
        if num not in unique_nums:
            result += num
    if result % 2 == 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:]
