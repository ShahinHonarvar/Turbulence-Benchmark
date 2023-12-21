
def all_ints_div_by_both_two_nums(my_list):
    # initialize an empty list to store the result
    result = []

    # loop through the specified range of indices in the input list
    for i in range(34, 70):
        # check if the current element is divisible by both 19 and 32
        if my_list[i] % 19 == 0 and my_list[i] % 32 == 0:
            # if it is, add it to the result list
            result.append(my_list[i])

    # return the result list
    return result
