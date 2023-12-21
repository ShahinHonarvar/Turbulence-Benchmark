
def all_ints_div_by_both_two_nums(my_list):
    # initialize an empty list to store the results
    result = []

    # loop through the specified range of indices in the input list
    for i in range(30, 201):

        # check if the current element is divisible by both -115 and 115
        if my_list[i] % (-115) == 0 and my_list[i] % (115) == 0:

            # if it is, add it to the result list
            result.append(my_list[i])

    # return the result list
    return result
