
def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[99]
    
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[87:99]:
            sum += i
    
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
