
def find_second_smallest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Get the smallest element
    smallest = my_list[0]

    # Iterate through the list and find the second smallest element
    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]

    # Return the second smallest element
    return smallest
