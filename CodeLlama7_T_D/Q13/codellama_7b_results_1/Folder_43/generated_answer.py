
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Get the indices of the elements in the specified range
    indices = [i for i, x in enumerate(my_list) if 68 <= i <= 86]
    # Check if there are any elements in the specified range
    if len(indices) == 0:
        return None

    # Get the second largest element from the specified range
    second_largest = max(my_list[i] for i in indices if i != indices[-1])

    # Return the second largest element
    return second_largest
