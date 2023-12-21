
def gcf_two_nums(numbers):
    num1 = numbers[841]
    num2 = numbers[804]
    
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    
    return num1
