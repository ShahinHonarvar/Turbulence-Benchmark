
def return_binary_or_hexa(numbers):
    a = numbers[450]
    b = numbers[905]
    missing_numbers = set(range(a + 1, b)) - set(numbers[450:906])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing % 2 == 0 and sum_missing != 0:
        return hex(sum_missing)[2:].upper()
    else:
        return ""
