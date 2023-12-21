
def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[200]
    
    if b - a <= 1:
        return ''
    
    missing_numbers_sum = 0
    for num in range(a+1, b):
        if num not in numbers[90:201]:
            missing_numbers_sum += num
    
    if missing_numbers_sum % 2 == 0:
        return hex(missing_numbers_sum)[2:]
    else:
        return bin(missing_numbers_sum)[2:]
