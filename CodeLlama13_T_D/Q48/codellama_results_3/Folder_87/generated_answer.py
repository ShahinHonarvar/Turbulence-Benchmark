
def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[43]
    
    sum_odd = 0
    for i in range(a + 1, b - 1):
        if i not in numbers:
            sum_odd += 1
            
    if sum_odd % 2 == 0:
        return hex(sum_odd)
    else:
        return bin(sum_odd)[2:]
