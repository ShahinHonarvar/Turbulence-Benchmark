
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 64, 80 and 15
    num1 = my_list[64]
    num2 = my_list[80]
    num3 = my_list[15]
    gcf = 1

    for i in range(2, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
            gcf = i

    return gcf
