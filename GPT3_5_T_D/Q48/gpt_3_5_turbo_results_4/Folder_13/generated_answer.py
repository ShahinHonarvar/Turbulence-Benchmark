
def return_binary_or_hexa(numbers):
    a = numbers[46]
    b = numbers[91]

    total_sum = sum(numbers[a+1:b])

    missing_numbers = [n for n in range(a+1, b) if n not in numbers]

    if len(missing_numbers) == 0:
        return ""

    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
