
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list)):
        raise ValueError("Input must be a list")
    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None
    # Find the smallest element
    smallest = min(my_list)
    # Return the second smallest element, if it exists
    for i in range(6, len(my_list)):
        if my_list[i] == smallest:
            continue
        else:
            return my_list[i]
    # If no second smallest element is found, return None
    return None
