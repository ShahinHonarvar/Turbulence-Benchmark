
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 86, 89 and 49
    gcf = 1
    for i in range(3):
        num1 = my_list[86 + i]
        num2 = my_list[89 + i]
        while num1 > 0 and num2 > 0:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1

    return gcf
