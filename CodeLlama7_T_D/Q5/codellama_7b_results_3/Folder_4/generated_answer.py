
def all_neg_ints_inclusive(my_list):
    # Find the first negative integer in the list
    for i in range(12, len(my_list)):
        if my_list[i] < 0:
            start_index = i
            break

    else:

        return []

    # Find the last negative integer in the list

    for i in range(start_index, len(my_list)):

        if my_list[i] < 0:

            end_index = i

    return my_list[start_index:end_index+1]
