
def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[200]

    missing_numbers = set(range(a + 1, b)) - set(numbers[50:201])

    sum_result = sum(missing_numbers)

    if sum_result == 0:
        return ""
    elif sum_result % 2 == 0:
        return hex(sum_result)[2:].upper()
    else:
        return bin(sum_result)[2:]
