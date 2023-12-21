
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list, starting from index 639 and ending at index 975 (both inclusive)
    for i in range(639, 976):

        # If the current element is an odd integer, add it to the total sum
        if my_list[i] % 2 != 0:
            total += my_list[i]

    # Return the total sum of all odd integers in the specified range
    return total
