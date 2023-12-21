
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers from index 0 to index 3, both inclusive
    for i in range(4):

        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:

            # Add the current element to the total sum
            total += my_list[i]

    # Return the total sum of all even integers from index 0 to index 3, both inclusive
    return total
