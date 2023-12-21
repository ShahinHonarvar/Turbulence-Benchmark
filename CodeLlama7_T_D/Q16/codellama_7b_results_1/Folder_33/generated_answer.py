
def sum_even_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0

    # Iterate through the list from index 667 to index 774, both inclusive
    for i in range(667, 775):

        # If the current element is even, add it to the sum
        if my_list[i] % 2 == 0:
            sum += my_list[i]

    # Return the sum
    return sum
