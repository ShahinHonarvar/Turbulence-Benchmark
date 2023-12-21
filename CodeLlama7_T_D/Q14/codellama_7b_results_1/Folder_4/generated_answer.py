
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Check if the list is empty

    if len(my_list) == 0:
        return None

    # Initialize variables to keep track of the smallest and second smallest elements

    smallest = my_list[0]

    second_smallest = None

    # Iterate through the list starting from index 70

    for i in range(70, len(my_list)):

        # If the current element is smaller than the smallest element, update the smallest and second smallest elements

        if my_list[i] < smallest:

            second_smallest = smallest

            smallest = my_list[i]

        # If the current element is smaller than the smallest element and not equal to the second smallest element, update the second smallest element

        elif my_list[i] < second_smallest and my_list[i] != smallest:

            second_smallest = my_list[i]

    # Return the second smallest element if it exists, otherwise return 'None'

    if second_smallest is not None:

        return second_smallest


    else:

        return None
