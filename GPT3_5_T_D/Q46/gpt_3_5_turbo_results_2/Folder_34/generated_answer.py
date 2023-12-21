
def gcf_three_nums(numbers):
    num1 = numbers[53]
    num2 = numbers[23]
    num3 = numbers[45]
    
    while(num2):
        num1, num2 = num2, num1 % num2
        
    while(num3):
        num1, num3 = num3, num1 % num3
        
    return num1
