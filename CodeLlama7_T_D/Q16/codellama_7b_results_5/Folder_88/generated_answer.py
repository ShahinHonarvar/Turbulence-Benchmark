
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list of integers, starting from index 4 and ending at index 8 (inclusive)
    for i in range(4, 9):
        # If the current integer is even, add it to the total
        if my_list[i] % 2 == 0:
            total += my_list[i]
    # Return the sum of all even integers in the specified range, or 0 if no such integers exist
    return total
