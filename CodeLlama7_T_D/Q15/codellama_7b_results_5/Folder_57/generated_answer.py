
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Iterate through the list from index 27 to index 55, inclusive
    for i in range(27, 56):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the current element to the sum
            sum += my_list[i]

    # Return the sum of all odd integers from index 27 to index 55, inclusive
    return sum
