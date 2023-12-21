
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list, starting at index 91 and ending at index 99 (both inclusive)
    for i in range(91, 100):

        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:

            # If it is, add it to the total
            total += my_list[i]

    # Return the sum of all odd integers from index 91 to index 99 (both inclusive)
    return total
