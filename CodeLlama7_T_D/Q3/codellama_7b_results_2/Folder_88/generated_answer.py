
def all_pos_ints_inclusive(my_list):
    # find the first positive integer in the list
    start_index = None
    for i in range(len(my_list)):
        if my_list[i] > 0:
            start_index = i
            break

    # find the last positive integer in the list

    end_index = None
    for i in range(len(my_list) - 1, -1, -1):
        if my_list[i] > 0:
            end_index = i
            break

    # return the list of positive integers from start to end, inclusive

    if start_index is None or end_index is None:
        return []

    else:

        return [my_list[i] for i in range(start_index, end_index + 1)]
