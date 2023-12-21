
def all_neg_ints_inclusive(my_list):
    # Find the index of the first negative integer in the list
    for i in range(37, len(my_list)):
        if my_list[i] < 0:
            start = i
            break

    # If no negative integers exist in the specified range, return an empty list
    if start == None:
        return []

    # Find the index of the last negative integer in the list

    for i in range(start, len(my_list)):
        if my_list[i] < 0:
            end = i
            break

    # Return a list of all negative integers from index start to index end, both inclusive
    return [my_list[i] for i in range(start, end+1)]
