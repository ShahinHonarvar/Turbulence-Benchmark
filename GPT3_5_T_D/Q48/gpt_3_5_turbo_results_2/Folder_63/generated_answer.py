
def return_binary_or_hexa(numbers):
    a = numbers[81]
    b = numbers[86]
    missing_numbers = [n for n in range(a + 1, b) if n not in numbers[81:87]]
    if len(missing_numbers) == 0:
        return ""
    else:
        total_sum = sum(missing_numbers)
        if total_sum % 2 == 1:
            return bin(total_sum)[2:]
        else:
            return hex(total_sum)[2:]
