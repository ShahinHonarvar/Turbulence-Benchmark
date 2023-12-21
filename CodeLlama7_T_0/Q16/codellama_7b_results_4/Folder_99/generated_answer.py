
def sum_even_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    total = 0

    # Iterate through the list, starting from index 310 and ending at index 370 (both inclusive)
    for i in range(310, 371):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            total += my_list[i]

    # Return the sum of all even integers from index 310 to index 370 (both inclusive), or 0 if no even integers exist in the specified range.
    return total
