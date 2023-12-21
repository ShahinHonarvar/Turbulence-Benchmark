
def find_second_smallest_num(my_list):
    # Check if the list has enough elements
    if len(my_list) < 86:
        return None

    # Find the smallest element in the range
    smallest = my_list[75]
    for i in range(76, 86):
        if my_list[i] < smallest:
            smallest = my_list[i]

    # Return the second smallest element
    for i in range(75, 85):
        if my_list[i] == smallest:
            return my_list[i + 1]

    # If no such element exists, return None
    return None
