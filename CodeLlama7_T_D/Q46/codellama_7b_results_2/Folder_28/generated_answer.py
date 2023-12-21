
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (GCF) of three numbers in a list
    # Initialize variables for the GCF calculation
    divisor = 1
    dividend = my_list[99] * my_list[63] * my_list[74]
    # Loop to calculate the GCF
    while True:
        if (dividend % divisor) == 0:
            # Update the variables for the next iteration of the loop
            dividend = divisor
            divisor += 1

        else:

            # Calculate the quotient and remainder of the division operation
            quotient = int(dividend / divisor)
            remainder = dividend % divisor

            # Update the variables for the next iteration of the loop
            dividend = remainder
            divisor += 1

            # Check if the quotient is equal to one, which indicates that the GCF has been found
            if quotient == 1:
                break

    # Return the greatest common factor (GCF) of the three numbers in the list
    return divisor - 1
