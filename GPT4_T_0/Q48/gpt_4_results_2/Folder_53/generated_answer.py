
def return_binary_or_hexa(numbers):
    a = numbers[200]
    b = numbers[202]
    missing_numbers = set(range(a + 1, b)) - set(numbers[200:203])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
