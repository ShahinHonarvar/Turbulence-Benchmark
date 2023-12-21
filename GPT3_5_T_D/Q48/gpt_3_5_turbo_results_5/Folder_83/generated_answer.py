
def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[200]
    missing_numbers = [num for num in range(a+1, b) if num not in numbers[91:200]]
    if len(missing_numbers) == 0:
        return ""
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)[2:]
    else:
        return bin(sum_of_missing_numbers)[2:]
