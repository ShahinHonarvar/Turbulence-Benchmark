
def return_binary_or_hexa(input_tuple):
    a = input_tuple[13]
    b = input_tuple[76]

    absent_values = set(range(a+1, b)) - set(input_tuple[13:77])
    total_sum = sum(absent_values)

    if total_sum == 0:
        return ''

    elif total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()

    else:
        return bin(total_sum)[2:]
