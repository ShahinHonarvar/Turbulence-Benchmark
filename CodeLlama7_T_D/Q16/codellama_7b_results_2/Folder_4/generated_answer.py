
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers, starting from index 12 and ending at index 92
    for i in range(12, 92 + 1):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the total sum
            total += my_list[i]

    # Return the total sum of all even integers in the specified range
    return total
