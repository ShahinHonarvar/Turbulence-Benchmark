
def return_binary_or_hexa(input_tuple):
    a = input_tuple[62]
    b = input_tuple[96]

    exclusive_range_sum = sum(set(range(a + 1, b)) - set(input_tuple[62:96]))

    if exclusive_range_sum == 0:
        return ''
    elif exclusive_range_sum % 2 == 0:
        return hex(exclusive_range_sum)[2:]
    else:
        return bin(exclusive_range_sum)[2:]
