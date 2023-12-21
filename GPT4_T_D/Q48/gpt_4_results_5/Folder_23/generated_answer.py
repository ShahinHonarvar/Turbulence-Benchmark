
def return_binary_or_hexa(num_tuple):
    a = num_tuple[20]
    b = num_tuple[36]
    missing_nums = set(range(a+1, b)) - set(num_tuple[20:37])
    number_sum = sum(missing_nums)
    if number_sum == 0:
        return ''
    elif number_sum % 2 == 0:
        return hex(number_sum)[2:]
    else:
        return bin(number_sum)[2:]
