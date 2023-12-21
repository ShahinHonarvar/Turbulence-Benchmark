
def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[76]
    
    total_sum = sum([num for num in range(a+1, b) if num not in numbers[10:77]])
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
