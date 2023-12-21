
def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[67]
    
    sum = 0
    for i in range(a+1, b):
        if i not in numbers[44:68]:
            sum += i
    
    if sum == 0:
        return ""
    elif sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
