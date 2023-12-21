
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers, starting from index 50 and ending at index 54
    for i in range(50, 55):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is, add it to the total
            total += my_list[i]

    # Return the sum of all even integers in the specified range
    return total
