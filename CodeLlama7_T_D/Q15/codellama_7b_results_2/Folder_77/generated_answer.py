
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers
    for i in range(527, 539):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the total sum
            total += my_list[i]

    # Return the total sum of all odd integers in the specified range
    return total
