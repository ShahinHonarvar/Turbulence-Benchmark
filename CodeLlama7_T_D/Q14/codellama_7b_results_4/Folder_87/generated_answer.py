
def find_second_smallest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Sort the list in ascending order
    my_list.sort()

    # Initialize variables to keep track of the smallest and second smallest elements
    smallest = my_list[0]
    second_smallest = None

    # Iterate through the list from index 22 to index 88, both inclusive
    for i in range(22, 90):
        if my_list[i] < smallest:
            second_smallest = smallest
            smallest = my_list[i]

    # If there is no such element, return 'None'
    if second_smallest == None:
        return None

    # Otherwise, return the second smallest element
    else:
        return second_smallest
