
def return_binary_or_hexa(lst):
    a = lst[18]
    b = lst[52]
    missing_numbers = set(range(a + 1, b)) - set(lst[18:53])
    sum_missing = sum(missing_numbers)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
