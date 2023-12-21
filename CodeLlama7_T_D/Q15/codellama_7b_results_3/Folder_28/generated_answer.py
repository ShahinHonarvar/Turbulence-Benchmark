
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Iterate over the list of integers from index 62 to index 63, both inclusive
    for i in range(62, 64):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the current element to the sum
            sum += my_list[i]

    # Return the sum of all odd integers from index 62 to index 63, both inclusive. If no odd integers exist in the specified range, the function should return 0.
    return sum
