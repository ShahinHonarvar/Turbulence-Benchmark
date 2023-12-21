
def return_binary_or_hexa(numbers):
    a = numbers[55]
    b = numbers[84]
    missing_numbers = set(range(a + 1, b)) - set(numbers[55:85])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()
