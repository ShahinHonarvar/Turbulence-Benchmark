
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list
    for i in range(56, len(my_list)):
        if my_list[i] > 0:
            start = i
            break

    else:

        return []

    # Find the last positive integer in the list

    for i in range(start, len(my_list)):
        if my_list[i] > 0:
            end = i

    # Return the list of all positive integers from start to end

    return [x for x in my_list[start:end+1] if x > 0]
