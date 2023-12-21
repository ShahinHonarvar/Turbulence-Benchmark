 `def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 654, 312 and 441
    num1 = my_list[654]
    num2 = my_list[312]
    num3 = my_list[441]
    gcf = 1

    for i in range(2, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
            gcf = i

    return gcf`
