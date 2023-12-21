
def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[5]
    missing_numbers = [x for x in range(a + 1, b) if x not in numbers[2:6]]

    if not missing_numbers:
        return ''

    sum_of_missing_numbers = sum(missing_numbers)

    if sum_of_missing_numbers % 2 != 0:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()
