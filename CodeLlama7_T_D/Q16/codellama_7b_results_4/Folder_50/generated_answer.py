
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list from index 70 to index 84, both inclusive
    for i in range(70, 85):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the sum
            total += my_list[i]

    # Return the sum
    return total
