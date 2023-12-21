
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the list and check if each element is between 266 and 586, both inclusive
    for i in my_list:
        if 266 <= i <= 586:
            # If the element is between the given range, add it to the sum
            total += i

    # Return the sum
    return total
