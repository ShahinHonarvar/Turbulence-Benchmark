
def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[8]
    total_sum = sum(numbers[a+1:b])
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
