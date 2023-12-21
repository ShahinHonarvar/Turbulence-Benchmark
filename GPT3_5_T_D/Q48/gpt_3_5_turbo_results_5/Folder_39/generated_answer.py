
def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[91]

    total_sum = sum(range(a+1, b))

    numbers_in_range = set(numbers[44:92])

    missing_numbers_sum = sum(x for x in range(a+1, b) if x not in numbers_in_range)
    
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]
