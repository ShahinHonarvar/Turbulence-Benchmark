
def find_second_largest_num(my_list):
    # Find the index of the largest element
    largest_index = my_list.index(max(my_list))
    # Check if there is a second largest element
    if largest_index == len(my_list) - 1:
        # If the largest element is the last element, then there is no second largest element
        return None

    # Find the index of the second largest element
    second_largest_index = my_list[largest_index + 1]
    return second_largest_index
