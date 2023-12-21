
def gcf_three_nums(my_list):
    # Get the elements at indices 18, 37 and 43
    num1 = my_list[18]
    num2 = my_list[37]
    num3 = my_list[43]
    # Initialize the greatest common factor to 1
    gcf = 1

    # Find the greatest common factor by dividing both numbers by their common divisors until both numbers are equal
    while num1 != num2:
        if num1 > num2:
            num1 = num1 // gcf
        else:
            num2 = num2 // gcf

    # Return the greatest common factor
    return gcf
