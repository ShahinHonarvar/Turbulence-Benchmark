
def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[54]
    
    missing_numbers = []
    for i in range(a + 1, b):
        if i not in numbers[36:55]:
            missing_numbers.append(i)
    
    if len(missing_numbers) == 0:
        return ''
    
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
