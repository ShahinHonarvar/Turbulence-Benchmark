
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list, starting from index 5
    for i in range(len(my_list)):
        # If the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add it to the sum
            total += my_list[i]
    return total
