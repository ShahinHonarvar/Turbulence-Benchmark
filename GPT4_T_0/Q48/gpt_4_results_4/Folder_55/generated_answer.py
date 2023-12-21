
def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[12]
    missing_numbers = set(range(a + 1, b)) - set(numbers[10:13])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()
