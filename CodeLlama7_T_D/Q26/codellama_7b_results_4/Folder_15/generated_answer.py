
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list and check if each element is between 6 and 9
    for i in my_list:
        if 6 <= i <= 9:
            # If it is, add it to the total
            total += i

    # Return the sum
    return total
