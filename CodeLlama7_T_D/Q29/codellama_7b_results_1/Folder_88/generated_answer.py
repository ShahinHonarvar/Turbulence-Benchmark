 `def gcf_two_nums(my_list):
    num1 = my_list[27]
    num2 = my_list[34]
    if num1 == num2:
        return num1

    while num1 != num2:
        if num1 > num2:
            num1 -= num2

        else:
            num2 -= num1

    return num1
