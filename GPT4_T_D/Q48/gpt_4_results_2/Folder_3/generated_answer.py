
def return_binary_or_hexa(tuple_input):
    a = tuple_input[56]
    b = tuple_input[88]

    missing_nums_sum = sum(range(a + 1, b)) - sum(tuple_input[57:88])

    if missing_nums_sum == 0:
        return ''

    elif missing_nums_sum % 2 == 0:
        return hex(missing_nums_sum)[2:].upper()

    else:
        return bin(missing_nums_sum)[2:]
