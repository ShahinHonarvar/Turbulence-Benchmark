 
def gcf_three_nums(numbers):
    num1 = numbers[20]
    num2 = numbers[35]
    num3 = numbers[74]
    
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    
    while num3 != 0:
        temp = num3
        num3 = num1 % num3
        num1 = temp
        
    return num1
