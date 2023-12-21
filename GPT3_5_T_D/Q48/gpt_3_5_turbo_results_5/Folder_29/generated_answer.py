
def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[98]
    
    total = 0
    for i in range(a + 1, b):
        if i not in numbers[70:99]:
            total += i
    
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
