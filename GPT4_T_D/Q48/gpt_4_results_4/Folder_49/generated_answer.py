
def return_binary_or_hexa(input_tuple):
    a, b = input_tuple[80], input_tuple[200]
    missing_values = set(range(a+1, b)) - set(input_tuple[80:201])
    result_sum = sum(missing_values)
    if result_sum == 0:
        return ''
    elif result_sum % 2 == 0:
        return hex(result_sum)[2:]
    else:
        return bin(result_sum)[2:]
