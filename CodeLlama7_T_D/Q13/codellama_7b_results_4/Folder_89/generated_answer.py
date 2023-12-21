
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Check if the list is empty
    if len(my_list) == 0:
        return None
    # Initialize variables for keeping track of the second largest element and its index
    second_largest = None
    second_largest_index = -1
    # Iterate over the elements of the list
    for i in range(len(my_list)):
        # Check if the current element is the second largest element
        if my_list[i] > second_largest:
            # If it is, update the variables
            second_largest = my_list[i]
            second_largest_index = i
    # Return the second largest element and its index
    return (second_largest, second_largest_index)
