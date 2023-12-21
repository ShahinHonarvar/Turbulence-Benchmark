
def return_binary_or_hexa(tuple_vals):
    a = tuple_vals[86]
    b = tuple_vals[89]
    integer_sum = sum(set(range(a + 1, b)) - set(tuple_vals[86:90]))
    if integer_sum % 2 == 0:
        return format(integer_sum, 'x')
    else:
        return format(integer_sum, 'b')
