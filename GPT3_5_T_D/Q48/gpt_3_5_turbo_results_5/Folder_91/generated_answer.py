
def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[6]
    total = 0
    
    for i in range(a+1, b):
        if i not in numbers[1:6]:
            total += i
    
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
