
def find_second_smallest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Find the second smallest number by sorting the list and returning the second element
    my_list.sort()
    return my_list[1]
