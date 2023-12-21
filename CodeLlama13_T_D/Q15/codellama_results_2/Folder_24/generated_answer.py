
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum
    sum = 0
    # Iterate through the list and check if the current index is odd
    for i in range(74, 96):
        if my_list[i] % 2 == 1:
            # If it is odd, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
