
def return_binary_or_hexa(numbers):
    a = numbers[55]
    b = numbers[84]
    
    missing_numbers = []
    for i in range(a+1, b):
        if i not in numbers[55:85]:
            missing_numbers.append(i)
    
    if not missing_numbers:
        return ""
    
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
