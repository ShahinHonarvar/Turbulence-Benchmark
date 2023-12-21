 
def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[200]
    range_sum = 0
    
    for i in range(a + 1, b):
        if i not in numbers[60:201]:
            range_sum += i
    
    if range_sum == 0:
        return ''
    elif range_sum % 2 == 0:
        return hex(range_sum)[2:]
    else:
        return bin(range_sum)[2:]
