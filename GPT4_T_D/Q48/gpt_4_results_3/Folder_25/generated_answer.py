
def return_binary_or_hexa(my_tuple):
    a, b = my_tuple[37], my_tuple[43]
    exclude_set = set(my_tuple[37:44])
    missing_values = set(range(a + 1, b)) - exclude_set
    my_sum = sum(missing_values)
    if my_sum == 0:
        return ""
    if my_sum % 2 == 1:
        return bin(my_sum)[2:]
    else:
        return hex(my_sum)[2:].upper()
