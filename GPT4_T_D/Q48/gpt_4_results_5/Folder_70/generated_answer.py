
def return_binary_or_hexa(numbers):
    a = numbers[43]
    b = numbers[70]

    missing_numbers = set(range(a + 1, b))
    missing_numbers.difference_update(numbers[43:71])

    if not missing_numbers:
        return ""

    sum_missing_numbers = sum(missing_numbers)

    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()
