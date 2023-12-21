
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 59, 93 and 84
    num1 = my_list[59]
    num2 = my_list[93]
    num3 = my_list[84]
    gcf = num1


    for i in range(2, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
            gcf = i


    return gcf
