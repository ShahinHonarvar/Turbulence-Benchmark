
def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[9]
    total_sum = sum([i for i in range(a + 1, b) if i not in numbers[6:10]])
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()
