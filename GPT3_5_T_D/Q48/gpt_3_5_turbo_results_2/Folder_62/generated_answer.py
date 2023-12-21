
def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[92]
    
    total_sum = 0
    
    for i in range(a+1, b):
        if i not in numbers[51:92]:
            total_sum += i
    
    if total_sum % 2 == 1:
        return format(total_sum, 'b')
    else:
        return format(total_sum, 'x')
