
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list from index 36 to index 46, both inclusive
    for i in range(36, 47):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
