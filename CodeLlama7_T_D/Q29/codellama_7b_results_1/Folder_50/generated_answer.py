
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by dividing both numbers by their least common multiple

    # Get the indices of the two numbers
    idx1 = 90
    idx2 = 54

    # Get the values of the two numbers
    num1 = my_list[idx1]
    num2 = my_list[idx2]

    # Find the least common multiple of the two numbers
    lcm = (num1 * num2) // math.gcd(num1, num2)

    # Divide both numbers by their least common multiple
    quotient1 = num1 // lcm
    quotient2 = num2 // lcm

    # Return the greatest common factor of the two numbers
    return math.gcd(quotient1, quotient2)
