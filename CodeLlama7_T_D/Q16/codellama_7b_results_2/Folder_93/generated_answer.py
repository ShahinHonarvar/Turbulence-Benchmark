
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list, starting from index 75 and ending at index 94
    for i in range(75, 95):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
