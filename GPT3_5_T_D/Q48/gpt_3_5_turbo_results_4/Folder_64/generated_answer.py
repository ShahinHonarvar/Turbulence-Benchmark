
def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[5]
    total_sum = 0
    
    for i in range(a + 1, b):
        if i not in numbers[1:5]:
            total_sum += i
    
    if total_sum == 0:
        return ""
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
