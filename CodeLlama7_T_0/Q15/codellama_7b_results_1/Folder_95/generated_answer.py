
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list from index 82 to index 86, both inclusive
    for i in range(82, 87):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the sum
            total += my_list[i]

    # Return the sum of all odd integers from index 82 to index 86, both inclusive
    return total
