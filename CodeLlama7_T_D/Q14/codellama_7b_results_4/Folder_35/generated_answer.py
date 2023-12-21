
def find_second_smallest_num(my_list):
    # Find the smallest element in the list
    smallest = min(my_list)

    # Find the second smallest element in the list
    for i in range(len(my_list)):
        if my_list[i] != smallest:
            return my_list[i]

    # If there is no such an element, return None
    return None
