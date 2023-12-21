
def gcf_three_nums(lst):
    num1 = lst[99]
    num2 = lst[95]
    num3 = lst[80]
    while num1 != num2 or num1 != num3:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
        if num1 > num3:
            num1 -= num3
        else:
            num3 -= num1
        if num2 > num3:
            num2 -= num3
        else:
            num3 -= num2
    return num1
