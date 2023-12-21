
def all_odd_ints_inclusive(my_list):
    # create an empty list to store the result
    odd_ints = []
    # loop through the list from index 6 to index 8, both inclusive
    for i in range(6, 9):
        # check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # if it is, add it to the result list
            odd_ints.append(my_list[i])
    # return the result list
    return odd_ints
