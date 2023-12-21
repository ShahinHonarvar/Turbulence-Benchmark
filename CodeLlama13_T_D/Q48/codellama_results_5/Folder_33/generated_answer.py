
def return_binary_or_hex(numbers):
    a = numbers[13]
    b = numbers[35]
    
    sum_odd = 0
    for i in range(a+1, b):
        if i not in numbers:
            sum_odd += i
    
    if sum_odd % 2 == 0:
        return hex(sum_odd)[2:]
    else:
        return bin(sum_odd)[2:]
