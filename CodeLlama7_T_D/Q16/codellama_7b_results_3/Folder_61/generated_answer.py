
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list of integers, starting from index 0
    for i in range(len(my_list)):

        # Check if the current element is even
        if my_list[i] % 2 == 0:

            # If it is, add it to the total sum
            total += my_list[i]

    # Return the total sum
    return total
