
def gcf_two_nums(numbers):
    num1 = numbers[793]
    num2 = numbers[449]
    
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    
    return num1
