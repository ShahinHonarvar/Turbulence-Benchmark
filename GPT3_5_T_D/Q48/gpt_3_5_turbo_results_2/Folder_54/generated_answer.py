
def return_binary_or_hexa(numbers):
    a = numbers[35]
    b = numbers[64]
    
    subset = set(numbers[36:64])
    
    total = 0
    for num in range(a+1, b):
        if num not in subset:
            total += num
    
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
