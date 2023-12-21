
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers, starting from index 8 and ending at index 9 (inclusive)
    for i in range(8, 10):

        # Check if the current element is even
        if my_list[i] % 2 == 0:

            # If it is even, add it to the total
            total += my_list[i]

    # Return the sum of all even integers in the specified range, or 0 if no such integers exist
    return total
