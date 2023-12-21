
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list, starting from index 19 and ending at index 92 (both inclusive)
    for i in range(19, 93):

        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:

            # If it is, add it to the total sum
            total += my_list[i]

    # Return the total sum of all even integers in the specified range, or 0 if no such integers exist
    return total
