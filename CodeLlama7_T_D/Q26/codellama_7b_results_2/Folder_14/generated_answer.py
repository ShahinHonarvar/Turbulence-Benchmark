
def sum_in_range(my_list):
    # Initialize the sum variable to 0
    sum = 0
    # Loop through each element in the list
    for element in my_list:
        # Check if the element is between 3 and 7, inclusive
        if 3 <= element <= 7:
            # If it is, add it to the sum
            sum += element

    # Return the sum
    return sum
