
def gcf_two_nums(numbers):
    num1 = numbers[20]
    num2 = numbers[83]
    
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
            
    return num1
