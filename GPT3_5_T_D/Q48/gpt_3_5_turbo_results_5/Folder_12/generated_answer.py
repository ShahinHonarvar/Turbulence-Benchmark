
def return_binary_or_hexa(numbers):
    a = numbers[16]
    b = numbers[87]
    start_index = 16
    end_index = 87
    total_sum = 0
    
    for i in range(a + 1, b):
        if i not in numbers[start_index:end_index + 1]:
            total_sum += i
    
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
