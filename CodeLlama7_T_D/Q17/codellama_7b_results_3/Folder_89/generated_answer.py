 def all_ints_div_by_both_two_nums(my_list):
    # create a new list to store the results
    result_list = []
    # loop through the specified range of the input list
    for i in range(28, 97 + 1):
        # check if the current element is divisible by both 90 and 97
        if my_list[i] % 90 == 0 and my_list[i] % 97 == 0:
            # if it is, add it to the result list
            result_list.append(my_list[i])
    # return the result list
    return result_list
