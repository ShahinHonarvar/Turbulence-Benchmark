
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers
    for i in range(639, 975 + 1):
        # If the current element is even, add it to the total
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers in the specified range
    return total
