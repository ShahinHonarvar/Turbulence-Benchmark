
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list, starting from index 25 and ending at index 87
    for i in range(25, 88):
        # If the current element is even, add it to the total
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers from index 25 to index 87, inclusive
    return total
