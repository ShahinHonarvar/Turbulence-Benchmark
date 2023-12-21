
def return_binary_or_hexa(numbers):
    a = numbers[22]
    b = numbers[24]
    total_sum = sum(numbers[a+1:b])
    missing_numbers = [num for num in range(a+1, b) if num not in numbers]
    if missing_numbers:
        return_string = ''
        if total_sum % 2 == 1:
            return_string = bin(total_sum)[2:]
        else:
            return_string = hex(total_sum)[2:]
        return return_string.upper()
    else:
        return ""
