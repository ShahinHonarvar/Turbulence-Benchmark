
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list of integers starting from index 75
    for i in range(75, len(my_list)):

        # If the current integer is even, add it to the total
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers from index 75 to index 94, both inclusive
    return total
