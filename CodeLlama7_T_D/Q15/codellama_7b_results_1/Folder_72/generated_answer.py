
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list, starting from index 29 and ending at index 51 (both inclusive)
    for i in range(29, 52):

        # If the current element is an odd integer, add it to the total
        if my_list[i] % 2 != 0:
            total += my_list[i]

    # Return the sum of all odd integers in the specified range, or 0 if no such integers exist
    return total
