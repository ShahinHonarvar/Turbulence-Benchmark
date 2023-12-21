
def return_binary_or_hexa(numbers):
    a = numbers[450]
    b = numbers[905]
    total_sum = 0
    
    for i in range(a + 1, b):
        if i not in numbers[451:905]:
            total_sum += i
    
    if total_sum % 2 == 1:
        return format(total_sum, 'b')
    else:
        return format(total_sum, 'X')
