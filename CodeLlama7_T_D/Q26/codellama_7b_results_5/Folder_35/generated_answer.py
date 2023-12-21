
def sum_in_range(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the elements of the list
    for element in my_list:
        # Check if the element is between 139 and 767
        if (element >= 139) and (element <= 767):
            # Add the element to the sum
            sum += element

    return sum
