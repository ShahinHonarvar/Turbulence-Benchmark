
def gcf_two_nums(lst):
    # Calculate the greatest common factor of the integers at indices 180 and 312
    num1 = lst[180]
    num2 = lst[312]

    while num2 != 0:
        num1, num2 = num2, num1 % num2

    return num1
