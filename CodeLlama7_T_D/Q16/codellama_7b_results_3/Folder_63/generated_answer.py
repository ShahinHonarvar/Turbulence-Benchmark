
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Loop through the list, starting from index 22 and ending at index 88 (inclusive)
    for i in range(22, 89):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers from index 22 to index 88 (inclusive)
    return total
