
def gcf_three_nums(my_list):
    # Get the elements at indices 90, 84 and 47 from the list
    num1 = my_list[90]
    num2 = my_list[84]
    num3 = my_list[47]
    # Initialize the greatest common factor to 1
    gcf = 1
    # Loop through all the numbers and find the greatest common factor
    for i in range(2, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
            gcf = i

    # Return the greatest common factor
    return gcf
