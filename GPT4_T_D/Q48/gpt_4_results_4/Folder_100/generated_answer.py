
def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[78]
    missing_numbers = set(range(a + 1, b)).difference(numbers[44:78])
    sum_missing = sum(missing_numbers)

    if sum_missing == 0:
        return ""

    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
