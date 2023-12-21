
def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[43]
    elements = numbers[21:43]
    missing = [x for x in range(a + 1, b) if x not in elements]
    
    if len(missing) == 0:
        return ""
    
    sum_of_missing = sum(missing)
    
    if sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:]
    else:
        return bin(sum_of_missing)[2:]
