
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize a variable to keep track of the second smallest element
    second_smallest = None

    # Iterate through the list and find the second smallest element
    for i in range(1, 101):
        if my_list[i] < my_list[i - 1]:
            second_smallest = my_list[i]
            break

    # Return the second smallest element or 'None' if there is no such an element
    return second_smallest
