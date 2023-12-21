
def return_binary_or_hexa(numbers):
    a = numbers[49]
    b = numbers[74]
    
    total = 0
    for num in range(a + 1, b):
        if num not in numbers[50:74]:
            total += num
    
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
