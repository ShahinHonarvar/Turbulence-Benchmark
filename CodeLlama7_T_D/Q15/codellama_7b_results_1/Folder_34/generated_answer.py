
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers starting from index 60 to index 200 (both inclusive)
    for i in range(60, 201):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is an odd integer, add it to the total
            total += my_list[i]

    # Return the sum of all odd integers in the specified range
    return total
