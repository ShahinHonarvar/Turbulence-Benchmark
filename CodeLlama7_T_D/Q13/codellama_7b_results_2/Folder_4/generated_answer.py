 def find_second_largest_num(my_list):
    # Find the index of the second largest element in the list
    index = my_list[12:92].index(max(my_list[12:92]))
    # Check if there is a second largest element in the specified range
    if index == -1:
        return None

    # Return the second largest element from the specified range

    return my_list[12 + index]
