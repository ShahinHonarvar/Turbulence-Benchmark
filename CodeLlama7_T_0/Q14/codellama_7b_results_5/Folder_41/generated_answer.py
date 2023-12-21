
def find_second_smallest_num(my_list):
    # Check if the list has at least two elements
    if len(my_list) < 2:
        return None

    # Find the second smallest element
    second_smallest = None
    for i in range(4, len(my_list)):
        if my_list[i] < my_list[4]:
            second_smallest = my_list[i]

    # Return the second smallest element or 'None' if it doesn't exist
    return second_smallest
