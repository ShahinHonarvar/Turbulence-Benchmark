
def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[60]
    missing_numbers = [x for x in range(a+1, b) if x not in numbers[18:61]]

    if len(missing_numbers) == 0:
        return ""

    sum_missing_numbers = sum(missing_numbers)
    
    if sum_missing_numbers % 2 == 0:
        return hex(sum_missing_numbers)[2:]
    else:
        return bin(sum_missing_numbers)[2:]
