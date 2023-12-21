
def return_binary_or_hexa(numbers):
    a = numbers[42]
    b = numbers[87]
    missing_numbers = set(range(a + 1, b)) - set(numbers[42:88])
    sum_missing = sum(missing_numbers)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()
