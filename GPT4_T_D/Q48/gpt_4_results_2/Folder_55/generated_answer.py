
def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[12]
    total_range = set(range(a + 1, b))
    tup_range = set(tup[10:12])
    missing_numbers = total_range - tup_range
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 0:
        return format(sum_missing_numbers, 'x')
    else:
        return format(sum_missing_numbers, 'b')
