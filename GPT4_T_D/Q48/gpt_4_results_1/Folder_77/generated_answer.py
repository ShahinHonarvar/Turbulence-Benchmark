
def return_binary_or_hexa(tuple_):
    a = tuple_[18]
    b = tuple_[52]
    missing_numbers = set(range(a + 1, b)) - set(tuple_[18:53])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers == 0:
        return ""
    elif sum_missing_numbers % 2 == 0:
        return hex(sum_missing_numbers)[2:]
    else:
        return bin(sum_missing_numbers)[2:]
