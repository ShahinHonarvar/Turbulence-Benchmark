
def return_binary_or_hexa(tup):
    a, b = tup[20], tup[93]
    missing_values_sum = sum(set(range(a + 1, b)) - set(tup[21:93]))
    if missing_values_sum % 2 == 1:
        return format(missing_values_sum, 'b')
    else:
        return format(missing_values_sum, 'X') if missing_values_sum != 0 else ''
