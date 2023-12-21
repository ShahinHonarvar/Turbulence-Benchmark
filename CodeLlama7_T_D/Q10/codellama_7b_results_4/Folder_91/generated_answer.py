
def all_odd_ints_exclusive(my_list):
    # initialize an empty list to store the odd integers
    odd_ints = []

    # loop through the list of integers
    for i in range(len(my_list)):
        # check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # add the odd integer to the list of odd integers
            odd_ints.append(my_list[i])

    # return the list of all odd integers from index 0 to index 5, both exclusive
    return odd_ints
