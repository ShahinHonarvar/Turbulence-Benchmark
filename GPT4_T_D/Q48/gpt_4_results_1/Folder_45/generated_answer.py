
def return_binary_or_hexa(tup):
    a = tup[30] + 1
    b = tup[200]
    missing_integers = [x for x in range(a, b) if x not in tup[30:201]]
    sum_miss_int = sum(missing_integers)
    if sum_miss_int % 2 == 0:
        return format(sum_miss_int, 'x')
    else:
        return format(sum_miss_int, 'b')
