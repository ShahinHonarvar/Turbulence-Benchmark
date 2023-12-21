
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list from index 5 to index 7, both inclusive
    for i in range(5, 8):

        # If the current element is an odd integer, add it to the total
        if my_list[i] % 2 != 0:
            total += my_list[i]

    # Return the sum of all odd integers from index 5 to index 7, both inclusive. If no odd integers exist in the specified range, return 0.
    return total
