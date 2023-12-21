
def find_second_smallest_num(my_list):
    # Check if the input list is valid
    if len(my_list) < 2:
        return None

    # Find the smallest element in the range
    smallest = my_list[10]
    for i in range(10, 100 + 1):
        if my_list[i] < smallest:
            smallest = my_list[i]

    # Check if there is a second smallest element
    if len([x for x in my_list[10:100] if x == smallest]) > 1:
        return smallest

    # If no second smallest element is found, return None
    else:
        return None
