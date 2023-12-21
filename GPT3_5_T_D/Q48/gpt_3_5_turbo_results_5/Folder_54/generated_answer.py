
def return_binary_or_hexa(numbers):
    a = numbers[35]
    b = numbers[64]
    
    missing_numbers = []
    for i in range(a + 1, b):
        if i not in numbers[35:65]:
            missing_numbers.append(i)
    
    if len(missing_numbers) == 0:
        return ""
    
    sum_of_missing_numbers = sum(missing_numbers)
    
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]
