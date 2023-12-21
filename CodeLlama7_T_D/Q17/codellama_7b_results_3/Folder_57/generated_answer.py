
def all_ints_div_by_both_two_nums(my_list):
    # initialize an empty list to store the result
    result = []

    # loop through the specified range of indices in my_list
    for i in range(51, 77 + 1):

        # check if the current element is divisible by both -90 and -59
        if my_list[i] % (-90) == 0 and my_list[i] % (-59) == 0:

            # if it is, add it to the result list
            result.append(my_list[i])

    # return the result list
    return result
