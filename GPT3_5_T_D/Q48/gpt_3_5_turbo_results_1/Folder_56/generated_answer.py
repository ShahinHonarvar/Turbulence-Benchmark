
def return_binary_or_hexa(numbers):
    a = numbers[7]
    b = numbers[9]
    total_sum = 0
    
    for i in range(a + 1, b):
        if i not in numbers[7:9]:
            total_sum += i
    
    if total_sum % 2 == 0:
        return hex(total_sum).lstrip('0x')
    else:
        return bin(total_sum).lstrip('0b')
