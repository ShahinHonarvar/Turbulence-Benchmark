
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers using the Euclidean algorithm
    a = my_list[96]
    b = my_list[57]
    c = my_list[85]
    # Initialize variables for the Euclidean algorithm
    old_a = 0
    new_a = 1
    old_b = 1
    new_b = 0
    # Perform the Euclidean algorithm until a and b are equal
    while (a != b):
        if (a > b):
            # Divide a by b and store the result in new_a
            new_a = a // b
            # Set old_a to a and set a to new_a
            old_a = a
            a = new_a
            # Multiply b by the difference between old_a and a and store the result in new_b
            new_b = b * (old_a - a)
            # Set old_b to b and set b to new_b
            old_b = b
            b = new_b
        else:
            # Divide b by a and store the result in new_b
            new_b = b // a
            # Set old_b to b and set b to new_b
            old_b = b
            b = new_b
    # Return the greatest common factor of a, b, and c
    return a * b * c
