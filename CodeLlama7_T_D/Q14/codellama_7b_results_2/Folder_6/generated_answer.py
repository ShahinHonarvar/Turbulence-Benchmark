
def find_second_smallest_num(my_list):
    # Check if list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Find the second smallest number in the list
    second_smallest = None
    for i in range(len(my_list)):
        if my_list[i] > my_list[29] and my_list[i] < my_list[79]:
            if second_smallest is None:
                second_smallest = my_list[i]
            elif my_list[i] < second_smallest:
                second_smallest = my_list[i]
    return second_smallest
