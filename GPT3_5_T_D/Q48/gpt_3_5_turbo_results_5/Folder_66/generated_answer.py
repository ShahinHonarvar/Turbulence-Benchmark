
def return_binary_or_hexa(numbers):
    a = numbers[11]
    b = numbers[76]
    missing_numbers = [num for num in range(a+1, b) if num not in numbers[12:76]]
    if missing_numbers:
        total_sum = sum(missing_numbers)
        if total_sum % 2 == 1:
            return bin(total_sum)[2:]
        else:
            return hex(total_sum)[2:].upper()
    else:
        return ""
