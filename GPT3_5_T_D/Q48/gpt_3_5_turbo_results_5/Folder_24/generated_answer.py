
def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[91]
    
    total_sum = 0
    
    for i in range(a + 1, b):
        if i not in numbers[13:92]:
            total_sum += i
    
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
