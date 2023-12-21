
def return_binary_or_hexa(numbers):
    a = numbers[49]
    b = numbers[74]
    excluded_numbers = set(range(a + 1, b)) - set(numbers[49:75])
    sum_excluded = sum(excluded_numbers)
    if sum_excluded % 2 == 1:
        return bin(sum_excluded)[2:]
    elif sum_excluded % 2 == 0 and sum_excluded != 0:
        return hex(sum_excluded)[2:].upper()
    else:
        return ""
