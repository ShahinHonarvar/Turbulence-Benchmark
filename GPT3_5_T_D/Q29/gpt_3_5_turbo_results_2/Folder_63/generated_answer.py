
def gcf_two_nums(lst):
    num1 = lst[21]
    num2 = lst[17]
    
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp

    return num1
