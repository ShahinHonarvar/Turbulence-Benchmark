
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers
    for i in range(50, 55):
        # If the current index is even
        if my_list[i] % 2 == 0:
            # Add the current integer to the sum
            total += my_list[i]

    # Return the sum of all even integers from index 50 to index 54, both inclusive
    return total
