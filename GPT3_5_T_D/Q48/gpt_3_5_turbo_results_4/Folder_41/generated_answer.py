
def return_binary_or_hexa(numbers):
    a = numbers[3]
    b = numbers[8]
    total = 0
    for i in range(a + 1, b):
        if i not in numbers[4:8]:
            total += i
            
    if total % 2 == 0:
        return hex(total)[2:]  # Remove '0x' prefix
    else:
        return bin(total)[2:]  # Remove '0b' prefix
