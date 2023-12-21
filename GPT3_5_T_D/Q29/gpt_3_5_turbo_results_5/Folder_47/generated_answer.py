
def gcf_two_nums(integers):
    num1 = integers[28]
    num2 = integers[17]
    
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    
    return num1
