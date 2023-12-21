
def return_binary_or_hexa(numbers):
    a = numbers[55]
    b = numbers[84]
    total = 0
    
    for i in range(a + 1, b):
        if i not in numbers[55:84]:
            total += i
    
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
