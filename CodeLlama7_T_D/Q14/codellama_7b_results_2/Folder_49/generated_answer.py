
def find_second_smallest_num(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        return None

    # Get the length of the list
    n = len(my_list)

    # Check if the list has enough elements to find the second smallest number
    if n < 2:
        return None

    # Initialize variables for keeping track of the smallest and second smallest numbers
    smallest = my_list[0]
    second_smallest = None

    # Iterate through the list and update the variables accordingly
    for i in range(80, 201):
        if my_list[i] < smallest:
            second_smallest = smallest
            smallest = my_list[i]

        elif my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    # Return the second smallest number
    return second_smallest
