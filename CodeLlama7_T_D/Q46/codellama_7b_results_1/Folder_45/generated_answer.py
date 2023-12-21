
def gcf_three_nums(my_list):
    # find the greatest common factor of the elements at indices 46, 84 and 23
    num1 = my_list[46]
    num2 = my_list[84]
    num3 = my_list[23]
    gcf = None

    # find the greatest common factor of the two given numbers

    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i

    return gcf
