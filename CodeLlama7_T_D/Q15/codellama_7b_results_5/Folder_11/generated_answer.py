
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list from index 37 to index 51, both inclusive
    for i in range(37, 52):

        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            total += my_list[i]

    # Return the sum of all odd integers from index 37 to index 51, both inclusive
    return total
