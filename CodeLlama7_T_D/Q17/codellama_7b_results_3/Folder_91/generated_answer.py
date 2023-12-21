
def all_ints_div_by_both_two_nums(my_list):
    # create an empty list to store the result
    result = []

    # loop through the specified range of indices in the input list
    for i in range(len(my_list))[:4]:

        # check if the current integer is divisible by both 8 and -3
        if my_list[i] % 8 == 0 and my_list[i] % (-3) == 0:

            # if it is, add it to the result list
            result.append(my_list[i])

    # return the result list
    return result
