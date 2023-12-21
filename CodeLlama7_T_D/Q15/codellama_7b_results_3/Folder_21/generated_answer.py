
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Loop through the list from index 639 to index 975, both inclusive
    for i in range(639, 976):

        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            sum += my_list[i]

    # Return the sum of all odd integers in the specified range, or 0 if no odd integers exist
    return sum
