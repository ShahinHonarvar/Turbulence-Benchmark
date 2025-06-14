
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")

    # Check if the list has at least two elements

    if len(my_list) < 2:
        raise ValueError("List must have at least two elements")

    # Initialize variables to keep track of the smallest and second smallest elements

    smallest = None

    second_smallest = None

    # Iterate through the list and find the smallest and second smallest elements

    for i in range(len(my_list)):
        if smallest is None or my_list[i] < smallest:
            second_smallest = smallest

            smallest = my_list[i]

        elif second_smallest is None or my_list[i] < second_smallest:
            second_smallest = my_list[i]

    # Return the second smallest element if it exists, otherwise return 'None'

    if second_smallest is not None:
        return second_smallest

    else:

        return None
