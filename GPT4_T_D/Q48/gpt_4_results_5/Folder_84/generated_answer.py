
def return_binary_or_hexa(tuple_of_ints):
    a = tuple_of_ints[32]
    b = tuple_of_ints[44]

    missing_ints = set(range(a + 1, b)) - set(tuple_of_ints[33:44])

    missing_sum = sum(missing_ints)

    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]
