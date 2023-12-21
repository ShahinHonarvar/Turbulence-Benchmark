
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Loop through the list of integers
    for i in range(56, 83):
        # Check if the current index is odd
        if my_list[i] % 2 != 0:
            # If it is odd, add it to the sum
            sum += my_list[i]

    # Return the sum of all odd integers from index 56 to index 82, both inclusive
    return sum
