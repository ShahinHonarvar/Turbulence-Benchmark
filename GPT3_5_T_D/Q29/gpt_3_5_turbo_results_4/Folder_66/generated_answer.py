
def gcf_two_nums(integers):
    num1 = integers[86]
    num2 = integers[89]
    
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    
    return num1
