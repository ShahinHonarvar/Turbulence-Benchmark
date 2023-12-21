
def return_binary_or_hexa(numbers):
    a = numbers[51]
    b = numbers[76]
    lst = numbers[52:76]
    total_sum = sum([i for i in range(a + 1, b) if i not in lst])
    
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
