
def gcf_two_nums(numbers):
    num1 = numbers[38]
    num2 = numbers[77]
    
    while num2:
        num1, num2 = num2, num1 % num2
    
    return num1
