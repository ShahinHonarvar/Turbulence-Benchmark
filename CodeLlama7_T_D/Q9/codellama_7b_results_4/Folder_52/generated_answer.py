
def all_odd_ints_inclusive(my_list):
    # create a new list to store the odd integers
    odd_ints = []
    # loop through the indices of the list, starting from index 28
    for i in range(28, len(my_list)):
        # if the current index's value is an odd integer, add it to the 'odd_ints' list
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    # return the 'odd_ints' list
    return odd_ints
