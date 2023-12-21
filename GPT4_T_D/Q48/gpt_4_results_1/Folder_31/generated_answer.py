
def return_binary_or_hexa(input_tuple):
    a, b = input_tuple[33], input_tuple[78]
    missing_values = set(range(a + 1, b)) - set(input_tuple[33:79])
    sum_missing_values = sum(missing_values)
    if sum_missing_values == 0:
        return ""
    return format(sum_missing_values, 'b') if sum_missing_values % 2 else format(sum_missing_values, 'X')
