
def return_binary_or_hexa(numbers):
    a = numbers[33]
    b = numbers[78]
    missing_numbers = set(range(a + 1, b)) - set(numbers[33:79])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()
