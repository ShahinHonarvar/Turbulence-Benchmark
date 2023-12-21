
def return_binary_or_hexa(tuple_numbers):
    a = tuple_numbers[20]
    b = tuple_numbers[200]
    missing_numbers = set(range(a+1, b)) - set(tuple_numbers[21:200])
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2 != 0:
        return bin(sum_of_missing)[2:]
    elif sum_of_missing == 0:
        return ""
    else:
        return hex(sum_of_missing)[2:]
