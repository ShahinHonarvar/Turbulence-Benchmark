
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers in a list
    num1 = my_list[16]
    num2 = my_list[87]
    num3 = my_list[95]
    if num1 == 0:
        return 0

    if num2 == 0:
        return 0

    if num3 == 0:
        return 0

    else:

        for i in range(1, min(num1, num2, num3) + 1):
            if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
                return i
