
def gcf_two_nums(num_list):
    num1 = num_list[27]
    num2 = num_list[34]
    
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    
    return num1
