
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    for i, x in enumerate(my_list):
        if x > 0:
            start = i
            break

    else:

        return []

    # Find the last positive integer in the list

    for i in range(len(my_list) - 1, -1, -1):
        if my_list[i] > 0:
            end = i
            break

    else:

        return []

    # Return the list of positive integers between start and end

    return [x for x in my_list[start:end + 1]]
