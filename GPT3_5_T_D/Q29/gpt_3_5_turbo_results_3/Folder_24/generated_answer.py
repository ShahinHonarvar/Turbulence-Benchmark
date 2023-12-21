
def gcf_two_nums(integers):
    num1 = integers[84]
    num2 = integers[21]
    
    while num2:
        num1, num2 = num2, num1 % num2
    
    return num1
