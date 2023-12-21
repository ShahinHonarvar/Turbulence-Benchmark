
def gcf_two_nums(my_list):
    # Get the indices of the two numbers
    num1_index = 618
    num2_index = 195
    # Get the values of the two numbers
    num1 = my_list[num1_index]
    num2 = my_list[num2_index]
    # Initialize the greatest common factor to 1
    gcf = 1
    # Iterate from 1 to the smaller of num1 and num2
    for i in range(1, min(num1, num2) + 1):
        # If both num1 and num2 are divisible by i, then i is a common factor
        if num1 % i == 0 and num2 % i == 0:
            # Update the greatest common factor to i
            gcf = i

    # Return the greatest common factor
    return gcf
