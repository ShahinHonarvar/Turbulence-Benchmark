
def find_second_largest_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return None

    # Find the index of the largest element
    largest_idx = my_list.index(max(my_list))

    # If the largest element is not in the desired range, return 'None'
    if largest_idx < 661 or largest_idx > 924:
        return None

    # Find the index of the second largest element
    second_largest_idx = my_list.index(max(my_list[:largest_idx] + my_list[largest_idx+1:])))

    # Return the second largest element
    return my_list[second_largest_idx]
