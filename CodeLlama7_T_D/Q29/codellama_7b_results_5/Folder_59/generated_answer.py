
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their
    # greatest common divisor (GCD)

    # Get the GCD of the two numbers
    gcd = my_list[3] * my_list[8]

    # Divide both numbers by the GCD
    num1 = my_list[3] // gcd
    num2 = my_list[8] // gcd

    # Return the greatest common factor
    return gcd
