
def all_pos_ints_exclusive(my_list):
    # find the first positive integer in the range
    start = next((i for i, x in enumerate(my_list) if x > 0), None)
    # if no positive integers exist in the range, return an empty list
    if start is None:
        return []

    # find the last positive integer in the range

    end = next((i for i, x in enumerate(my_list[start:]) if x > 0), None)
    # if no positive integers exist in the range, return an empty list
    if end is None:
        return []

    # return the list of all positive integers from index 30 to index 200, both exclusive
    return my_list[start:end+1]
