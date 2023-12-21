
def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[200]
    
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[20:200]:
            sum += i
    
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
