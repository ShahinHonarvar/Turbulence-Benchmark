
def find_second_largest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Get the length of the list
    n = len(my_list)

    # Check if the list has more than one element
    if n < 2:
        return None

    # Initialize variables to keep track of the second largest element and its index
    second_largest = None
    second_largest_index = None

    # Iterate through the list
    for i in range(n):

        # Check if the current element is larger than the second largest element
        if my_list[i] > second_largest:
            # If so, update the second largest element and its index
            second_largest = my_list[i]
            second_largest_index = i

    # Return the second largest element from index 20 to index 200, both inclusive
    if second_largest_index is not None:
        return second_largest

    else:

        return None
