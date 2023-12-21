
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    for i in range(41, len(my_list)):
        if my_list[i] > 0:
            start = i + 1
            break

    else:

        return []

    # Find the last positive integer in the list

    for i in range(start, len(my_list)):
        if my_list[i] > 0:
            end = i

    return my_list[start:end]
