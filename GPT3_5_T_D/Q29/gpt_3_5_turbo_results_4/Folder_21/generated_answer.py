
def gcf_two_nums(lst):
    num1 = lst[198]
    num2 = lst[212]
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1
