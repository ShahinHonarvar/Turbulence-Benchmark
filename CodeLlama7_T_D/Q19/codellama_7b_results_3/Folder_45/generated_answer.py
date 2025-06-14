
def all_ints_not_div_by_num(my_list):
    # create a new list to store the results
    result_list = []

    # loop through the list of integers
    for i in range(30, 200):
        # check if the current integer is not divisible by -115
        if my_list[i] % -115 != 0:
            # if it's not divisible, add it to the result list
            result_list.append(my_list[i])

    # return the result list
    return result_list
