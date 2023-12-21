
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0

    # Iterate through the list, starting from index 246 and ending at index 750 (inclusive)
    for i in range(246, 751):

        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:

            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum
    return sum
