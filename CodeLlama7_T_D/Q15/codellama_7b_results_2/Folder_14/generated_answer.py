
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Iterate through the list from index 5 to index 7
    for i in range(5, 8):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
