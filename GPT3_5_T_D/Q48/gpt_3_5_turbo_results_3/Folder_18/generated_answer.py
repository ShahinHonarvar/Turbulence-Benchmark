
def return_binary_or_hexa(numbers):
    a = numbers[56]
    b = numbers[90]
    missing_numbers = set(range(a + 1, b))
    for num in numbers[56:90]:
        missing_numbers.discard(num)
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()
