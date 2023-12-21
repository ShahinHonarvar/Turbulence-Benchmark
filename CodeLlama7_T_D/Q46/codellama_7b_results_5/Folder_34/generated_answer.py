
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 53, 23 and 45
    num1 = my_list[53]
    num2 = my_list[23]
    num3 = my_list[45]
    gcf = 1

    for i in range(2, min(num1, num2, num3) + 1):
        if (num1 % i == 0) and (num2 % i == 0) and (num3 % i == 0):
            gcf = i

    return gcf
