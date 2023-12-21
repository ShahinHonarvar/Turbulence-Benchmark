
def return_binary_or_hexa(tuple_):
    a = tuple_[77]
    b = tuple_[84]
    missing_numbers = set(range(a + 1, b)) - set(tuple_[77:85])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 0:
        return format(sum_missing_numbers, 'x')
    else:
        return format(sum_missing_numbers, 'b')
