
def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[91]
    total_sum = 0
    
    for i in range(a + 1, b):
        if i not in numbers[44:92]:
            total_sum += i
    
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
