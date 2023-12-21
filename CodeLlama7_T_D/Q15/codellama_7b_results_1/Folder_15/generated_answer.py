
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate through the list of integers
    for i in range(len(my_list))):
        # Check if the current integer is odd
        if my_list[i] % 2 != 0:
            # If it is, add it to the sum
            sum += my_list[i]
    return sum
