
def sum_in_range(my_list):
    # Initialize the sum to 0
    total = 0
    # Iterate over the elements in the list
    for element in my_list:
        # If the element is between 86 and 99, inclusive, add it to the sum
        if 86 <= element <= 99:
            total += element

    # Return the sum
    return total
