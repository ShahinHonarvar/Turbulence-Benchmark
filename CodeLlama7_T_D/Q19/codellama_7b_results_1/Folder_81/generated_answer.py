
def all_ints_not_div_by_num(my_list):
    # create a new list to store the result
    result = []

    # loop through the specified range of the input list
    for i in range(10, 100):

        # check if the current element is not divisible by 100
        if my_list[i] % 100 != 0:

            # if it's not divisible, add it to the result list
            result.append(my_list[i])

    # return the result list
    return result
