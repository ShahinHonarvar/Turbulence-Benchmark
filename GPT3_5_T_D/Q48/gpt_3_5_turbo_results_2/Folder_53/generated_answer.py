
def return_binary_or_hexa(numbers):
    a = numbers[200]
    b = numbers[202]
    total_sum = sum(numbers[a+1:b])
    missing_numbers = [num for num in range(a+1, b) if num not in numbers]
    if len(missing_numbers) == 0:
        return ""
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
