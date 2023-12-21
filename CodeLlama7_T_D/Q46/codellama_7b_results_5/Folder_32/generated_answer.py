 `def gcf_three_nums(my_list):
    # Extract the elements at indices 20, 43 and 95 from the input list
    num1 = my_list[20]
    num2 = my_list[43]
    num3 = my_list[95]
    # Initialize a variable to store the greatest common factor

    gcf = 1

    # Iterate through all the elements of the list

    for i in range(2, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
            gcf = i

    return gcf`
