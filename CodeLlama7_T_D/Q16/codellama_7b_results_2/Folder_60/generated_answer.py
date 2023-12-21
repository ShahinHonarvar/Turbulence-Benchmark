
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate through the list, starting from index 75 and ending at index 85 (both inclusive)
    for i in range(75, 86):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            total += my_list[i]
    # Return the sum of all even integers from index 75 to index 85 (both inclusive)
    return total
