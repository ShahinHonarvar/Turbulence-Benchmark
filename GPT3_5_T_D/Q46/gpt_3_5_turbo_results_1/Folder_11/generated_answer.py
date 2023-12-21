
def gcf_three_nums(arr):
    num1 = arr[37]
    num2 = arr[30]
    num3 = arr[48]
    
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    
    while num3 != 0:
        num1, num3 = num3, num1 % num3
    
    return num1
