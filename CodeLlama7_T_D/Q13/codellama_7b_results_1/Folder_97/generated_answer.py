
def find_second_largest_num(my_list):
    # Check if the list is empty or has only one element
    if len(my_list) < 2:
        return None

    # Find the index of the largest element
    largest_idx = my_list.index(max(my_list))

    # Check if the second largest element exists within the specified range
    if largest_idx - 40 >= 0 and largest_idx + 1 <= 80:
        return my_list[largest_idx - 40]

    # If the second largest element does not exist, return None
    return None
