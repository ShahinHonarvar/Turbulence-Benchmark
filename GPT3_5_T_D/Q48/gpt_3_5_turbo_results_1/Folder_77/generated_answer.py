
def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[52]
    
    total_sum = 0
    
    for i in range(a+1, b):
        if i not in numbers[19:52]:
            total_sum += i
    
    if total_sum % 2 == 0:
        return hex(total_sum).lstrip("0x")
    else:
        return bin(total_sum).lstrip("0b")
