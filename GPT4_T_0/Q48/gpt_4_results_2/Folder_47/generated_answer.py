
def return_binary_or_hexa(numbers):
    a = numbers[29]
    b = numbers[53]
    missing_numbers = set(range(a + 1, b)) - set(numbers[29:54])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()
