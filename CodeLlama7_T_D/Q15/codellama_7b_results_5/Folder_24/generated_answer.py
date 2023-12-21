
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list from index 74 to index 95, both inclusive
    for i in range(74, 96):

        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            total += my_list[i]

    # Return the sum of all odd integers from index 74 to index 95, both inclusive
    return total
