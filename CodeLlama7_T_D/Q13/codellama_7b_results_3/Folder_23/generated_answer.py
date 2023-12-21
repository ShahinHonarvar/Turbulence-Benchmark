
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Get the length of the list
    n = len(my_list)
    # Check if the input list is empty
    if n == 0:
        return None

    # Initialize variables to keep track of the second largest element and its index
    second_largest = None
    second_largest_index = -1

    # Iterate through the list and find the second largest element
    for i in range(n):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
            second_largest_index = i

    # Return the second largest element, or None if it is not found
    return second_largest if second_largest_index >= 52 and second_largest_index <= 71 else None
