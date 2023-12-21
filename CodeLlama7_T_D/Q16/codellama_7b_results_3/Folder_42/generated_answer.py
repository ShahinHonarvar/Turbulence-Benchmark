
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Loop through the list, starting from index 29 and ending at index 79
    for i in range(29, 80):
        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]
    # Return the sum
    return sum
