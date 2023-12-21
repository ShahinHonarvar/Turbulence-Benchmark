
def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[200]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers[71:200]:
            sum += i
    
    if sum == 0:
        return ""
    elif sum % 2 == 1:
        return bin(sum).replace('0b', '')
    else:
        return hex(sum).replace('0x', '')
