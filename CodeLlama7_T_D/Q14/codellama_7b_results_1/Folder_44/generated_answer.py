
def find_second_smallest_num(my_list):
    # Find the smallest element
    smallest = my_list[91]
    for i in range(92, 100):
        if my_list[i] < smallest:
            smallest = my_list[i]
    # Check if there is a second smallest element
    if len(my_list) > 100:
        return None

    # Return the second smallest element
    for i in range(91, 100):
        if my_list[i] == smallest:
            return my_list[i+1]
