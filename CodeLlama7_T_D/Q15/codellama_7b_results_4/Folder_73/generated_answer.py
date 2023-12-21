
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0

    # Loop through the list of integers, starting from index 19 and ending at index 92 (both inclusive)
    for i in range(19, 93):

        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            sum += my_list[i]

    # Return the sum of all odd integers from index 19 to index 92 (both inclusive), or 0 if no odd integers exist in the specified range.
    return sum
