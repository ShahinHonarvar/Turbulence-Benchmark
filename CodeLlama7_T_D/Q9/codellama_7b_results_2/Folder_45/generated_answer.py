
def all_odd_ints_inclusive(my_list):
    # create a new list to store the odd integers
    odd_ints = []
    # loop through the specified range of indices in the input list
    for i in range(30, 201):
        # check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # if it is, add it to the new list
            odd_ints.append(my_list[i])
    # return the new list of all odd integers in the specified range
    return odd_ints
