
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 90, 84 and 47
    gcf = 1
    for i in range(3):
        num1 = my_list[90 + i]
        num2 = my_list[84 + i]
        num3 = my_list[47 + i]
        if num1 > gcf and num2 > gcf and num3 > gcf:
            gcf = num1 * num2 * num3
    return gcf
