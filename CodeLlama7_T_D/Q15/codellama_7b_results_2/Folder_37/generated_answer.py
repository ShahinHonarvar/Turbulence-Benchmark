
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers from index 1 to index 5, both inclusive
    for i in range(1, len(my_list)):
        # If the current element is an odd integer, add it to the total
        if my_list[i] % 2 != 0:
            total += my_list[i]

    # Return the sum of all odd integers from index 1 to index 5, both inclusive. If no odd integers exist in the specified range, return 0.
    return total
