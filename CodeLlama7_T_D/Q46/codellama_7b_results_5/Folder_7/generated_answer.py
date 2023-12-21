 `def gcf_three_nums(my_list):
    # Get the elements at indices 477, 696 and 663
    num1 = my_list[477]
    num2 = my_list[696]
    num3 = my_list[663]
    # Initialize the greatest common factor to 1
    gcf = 1
    # Check if any of the numbers is divisible by the others
    for i in range(2, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
            gcf = i
            break

    return gcf`
