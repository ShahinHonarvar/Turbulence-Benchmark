
def return_binary_or_hexa(numbers):
    a = numbers[38]
    b = numbers[52]
    total = 0
    
    for num in range(a + 1, b):
        if num not in numbers[38:52]:
            total += num
    
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
