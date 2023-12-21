
def return_binary_or_hexa(numbers):
    a = numbers[6] + 1
    b = numbers[7]
    missing_values = [num for num in range(a, b) if num not in numbers[6:8]]
    sum_missing_values = sum(missing_values)
    if sum_missing_values % 2 != 0:
        return bin(sum_missing_values)[2:]
    elif sum_missing_values % 2 == 0 and sum_missing_values != 0:
        return hex(sum_missing_values)[2:].upper()
    return ''
