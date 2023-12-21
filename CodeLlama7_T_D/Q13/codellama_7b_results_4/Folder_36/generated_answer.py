
def find_second_largest_num(my_list):
    # Find the index of the second largest element in the list
    second_largest_index = None
    for i in range(246, 751):
        if my_list[i] > my_list[i-1]:
            if second_largest_index is None:
                second_largest_index = i
            elif my_list[i] > my_list[second_largest_index]:
                second_largest_index = i
    # Return the second largest element from index 246 to index 750, both inclusive
    if second_largest_index is not None:
        return my_list[second_largest_index]
    else:
        return None
