
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate over the list, starting from index 62 and ending at index 92
    for i in range(62, 93):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            total += my_list[i]
    # Return the sum of all even integers from index 62 to index 92
    return total
