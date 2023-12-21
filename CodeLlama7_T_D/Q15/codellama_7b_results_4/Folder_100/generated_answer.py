
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list from index 42 to 68 (both inclusive)
    for i in range(42, 69):
        # If the current element is an odd integer, add it to the total
        if my_list[i] % 2 != 0:
            total += my_list[i]

    # Return the sum of all odd integers from index 42 to index 68 (both inclusive), or 0 if no odd integers exist in the specified range.
    return total
