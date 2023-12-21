
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate through the list of integers from index 1 to index 5, both inclusive
    for i in range(1, 6):
        # If the current integer is odd, add it to the sum
        if my_list[i] % 2 != 0:
            sum += my_list[i]
    # Return the sum of all odd integers from index 1 to index 5, both inclusive. If no odd integers exist in the specified range, the function should return 0.
    return sum
