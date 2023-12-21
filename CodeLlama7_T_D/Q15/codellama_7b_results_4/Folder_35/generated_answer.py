
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Loop through the list from index 30 to 48
    for i in range(30, 49):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
