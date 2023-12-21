
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers, starting from index 56 and ending at index 98 (both inclusive)
    for i in range(56, 99):

        # Check if the current element is even

        if my_list[i] % 2 == 0:

            # If it is even, add it to the sum

            total += my_list[i]

    # Return the sum of all even integers in the specified range, or 0 if no such integers exist.

    return total
