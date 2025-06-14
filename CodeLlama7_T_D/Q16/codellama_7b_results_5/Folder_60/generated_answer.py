
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list from index 75 to index 85, both inclusive
    for i in range(75, 86):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the total
            total += my_list[i]

    # Return the sum of all even integers from index 75 to index 85, both inclusive
    return total
