
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list, starting from index 23 (inclusive)
    for i in range(23, len(my_list)):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the sum
            total += my_list[i]

    # Return the sum of all even integers from index 23 (inclusive) to the end of the list
    return total
