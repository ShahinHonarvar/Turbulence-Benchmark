
def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[44]
    total_sum = 0
    for num in range(a + 1, b):
        if num not in numbers[32:44]:
            total_sum += num
    
    if total_sum == 0:
        return ""
    
    if total_sum % 2 == 1:
        return format(total_sum, 'b')
    else:
        return format(total_sum, 'x')
