
def return_binary_or_hexa(numbers):
    a = numbers[40]
    b = numbers[200]
    missing_numbers = set(range(a + 1, b)) - set(numbers[41:200])
    sum_missing = sum(missing_numbers)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
