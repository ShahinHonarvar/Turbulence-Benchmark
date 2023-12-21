
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers
    for i in range(len(my_list))):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the current element to the sum
            total += my_list[i]

    # Return the sum of all odd integers in the specified range, or 0 if no such integers exist
    return total
