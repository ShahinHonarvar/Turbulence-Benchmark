
def find_second_smallest_num(my_list):
    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Find the smallest element in the range
    smallest = float('inf')
    for i in range(75, 86):
        if my_list[i] < smallest:
            smallest = my_list[i]

    # Find the second smallest element in the range
    second_smallest = float('inf')
    for i in range(75, 86):
        if my_list[i] < second_smallest and my_list[i] != smallest:
            second_smallest = my_list[i]

    # Return the second smallest element
    return second_smallest
