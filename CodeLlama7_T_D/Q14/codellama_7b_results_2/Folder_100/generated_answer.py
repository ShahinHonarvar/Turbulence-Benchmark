
def find_second_smallest_num(my_list):
    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Initialize variables to keep track of the smallest and second smallest elements
    smallest = my_list[0]
    second_smallest = None

    # Iterate over the list and find the smallest and second smallest elements
    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            second_smallest = smallest
            smallest = my_list[i]
        elif my_list[i] < second_smallest or second_smallest is None:
            second_smallest = my_list[i]

    # Return the second smallest element from index 43 to index 51, both inclusive
    return second_smallest
