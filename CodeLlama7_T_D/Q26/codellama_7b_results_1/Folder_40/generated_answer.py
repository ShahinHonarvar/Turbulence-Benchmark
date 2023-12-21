
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list
    for i in my_list:
        # Check if the current element is between -9 and -7
        if -9 <= i <= -7:
            # Add the element to the sum
            sum += i

    # Return the sum
    return sum
