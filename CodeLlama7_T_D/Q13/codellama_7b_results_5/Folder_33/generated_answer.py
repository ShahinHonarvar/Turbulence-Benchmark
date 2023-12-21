
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Initialize variables to keep track of the second largest element and its index
    second_largest = None
    second_largest_index = None

    # Iterate through the list and find the second largest element
    for i in range(len(my_list)):
        if my_list[i] > second_largest or second_largest is None:
            second_largest = my_list[i]
            second_largest_index = i

    # Return the second largest element and its index, or 'None' if no such element exists
    return second_largest, second_largest_index
