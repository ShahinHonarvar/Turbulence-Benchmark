
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (gcf) of the two input numbers
    num1 = my_list[38]
    num2 = my_list[77]
    if num1 > num2:
        smaller_num = num2
        larger_num = num1

    else:

        smaller_num = num1
        larger_num = num2

    # Initialize a variable to store the greatest common factor (gcf)
    gcf = 1

    # Iterate from 1 to the smaller number
    for i in range(1, smaller_num + 1):

        # Check if the current number is a factor of both numbers
        if num1 % i == 0 and num2 % i == 0:

            # If it is a factor, update the greatest common factor (gcf) variable
            gcf = i

    return gcf
