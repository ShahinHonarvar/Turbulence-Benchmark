
def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[85]
    sum = 0
    for i in range(a+1, b):
        if i not in numbers[36:86]:
            sum += i
    
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
