
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0

    # Iterate through the list of integers, starting from index 1 and ending at index 8 (inclusive)
    for i in range(1, len(my_list)):

        # If the current integer is even, add it to the sum
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers from index 1 to index 8 (inclusive)
    return total
