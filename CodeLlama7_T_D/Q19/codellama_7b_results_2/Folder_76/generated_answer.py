
def all_ints_not_div_by_num(my_list):
    # create a new list to store the results
    result = []

    # loop through the specified range of indices
    for i in range(361, 887):
        # if the current integer is not divisible by 877, add it to the results list
        if my_list[i] % 877 != 0:
            result.append(my_list[i])

    # return the results list
    return result
