
def gcf_two_nums(integers):
    num1 = integers[17]
    num2 = integers[20]
    
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
        
    return num1
