
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Check if the list is empty
    if len(my_list) == 0:
        return None
    # Sort the list in descending order
    my_list.sort(reverse=True)
    # Initialize the second largest element to None
    second_largest = None
    # Iterate over the elements in the list
    for i in range(len(my_list)):
        # Check if the current element is the second largest element
        if my_list[i] == my_list[i - 1]:
            second_largest = my_list[i]
    # Return the second largest element
    return second_largest
