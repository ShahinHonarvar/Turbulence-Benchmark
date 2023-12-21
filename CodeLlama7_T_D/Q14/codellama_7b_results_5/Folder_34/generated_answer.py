
def find_second_smallest_num(my_list):
    # Check if list is empty
    if len(my_list) == 0:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables to keep track of the smallest and second smallest elements
    smallest = my_list[0]
    second_smallest = None

    # Iterate through the list, starting from index 60, and find the second smallest element
    for i in range(len(my_list)):
        if i >= 60 and i <= 200:
            if my_list[i] < smallest:
                second_smallest = smallest
                smallest = my_list[i]
            elif my_list[i] < second_smallest or second_smallest is None:
                second_smallest = my_list[i]
    # Return the second smallest element, if it exists
    return second_smallest
