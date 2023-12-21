
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers
    # at indices 36, 85, and 83
    num1 = my_list[36]
    num2 = my_list[85]
    num3 = my_list[83]
    # Initialize the greatest common factor to 1
    gcf = 1

    for i in range(2, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
            gcf = i

    return gcf
