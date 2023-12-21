
def all_neg_ints_exclusive(my_list):
    # Find the first negative integer in the list
    for i in range(42, len(my_list)):
        if my_list[i] < 0:
            neg_int = my_list[i]
            break

    else:

        return []


    # Find the last negative integer in the list

    for i in range(len(my_list) - 1, 42, -1):
        if my_list[i] < 0:
            neg_int = my_list[i]
            break

    else:

        return []


    # Return the list of all negative integers in the specified range

    return [neg_int for neg_int in my_list if neg_int < 0 and (neg_int >= neg_int) and (neg_int <= neg_int)]
