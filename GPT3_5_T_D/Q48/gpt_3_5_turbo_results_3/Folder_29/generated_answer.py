

def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[98]

    missing_numbers = [x for x in range(a+1, b) if x not in numbers[70:98+1]]

    if len(missing_numbers) == 0:
        return ""

    total = sum(missing_numbers)

    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
