
def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[89]
    missing_numbers = set(range(a + 1, b)) - set(numbers[86:90])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()
