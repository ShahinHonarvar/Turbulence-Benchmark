
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list, starting from index 30 and ending at index 48
    for i in range(30, 49):

        # Check if the current element is even
        if my_list[i] % 2 == 0:

            # If it is even, add it to the total sum
            total += my_list[i]

    # Return the total sum
    return total
