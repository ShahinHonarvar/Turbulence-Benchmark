
def return_binary_or_hexa(t):
    a = t[29]
    b = t[53]
    missing_values = set(range(a+1, b)) - set(t[29:54])
    sum_missing_values = sum(missing_values)
    return '' if sum_missing_values == 0 else (format(sum_missing_values, 'b') if sum_missing_values % 2 != 0 else format(sum_missing_values, 'x'))
