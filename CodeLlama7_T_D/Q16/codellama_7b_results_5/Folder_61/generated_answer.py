
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0

    # Iterate over the list of integers, starting from index 0
    for i in range(len(my_list)):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the total sum
            total += my_list[i]

    # Return the total sum of all even integers in the specified range
    return total
