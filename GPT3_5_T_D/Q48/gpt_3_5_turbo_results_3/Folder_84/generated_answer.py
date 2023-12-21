
def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[44]
    
    sum = 0
    for i in range(a+1, b):
        if i not in numbers[32:44]:
            sum += i
    
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()
