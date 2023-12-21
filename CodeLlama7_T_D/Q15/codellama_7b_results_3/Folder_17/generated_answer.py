
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers, starting from index 62 and ending at index 78 (both inclusive)
    for i in range(62, 79):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the sum
            total += my_list[i]

    # Return the sum of all odd integers from index 62 to index 78 (both inclusive), or 0 if no such integers exist in the list.
    return total
