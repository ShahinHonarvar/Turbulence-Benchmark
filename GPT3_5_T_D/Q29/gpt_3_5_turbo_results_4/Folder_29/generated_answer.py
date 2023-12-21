
def gcf_two_nums(numbers):
    index1 = 96
    index2 = 57
    num1 = numbers[index1]
    num2 = numbers[index2]
    
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    
    return num1
