
def return_binary_or_hexa(numbers):
    a = numbers[43]
    b = numbers[70]
    total = sum(numbers[a+1:b])
    
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
