
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0
    # Iterate through the list, starting at index 14 and ending at index 64
    for i in range(14, 65):
        # If the current element is even, add it to the total
        if my_list[i] % 2 == 0:
            total += my_list[i]
    # Return the sum of all even integers from index 14 to index 64, inclusive
    return total
