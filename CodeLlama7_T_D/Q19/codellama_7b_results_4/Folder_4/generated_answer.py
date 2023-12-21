
def all_ints_not_div_by_num(my_list):
    # create a new list to store the result
    result = []

    # loop through the list of integers
    for i in range(len(my_list)):

        # if the current integer is not divisible by -36, add it to the result list
        if my_list[i] % -36 != 0:
            result.append(my_list[i])

    # return the result list
    return result
