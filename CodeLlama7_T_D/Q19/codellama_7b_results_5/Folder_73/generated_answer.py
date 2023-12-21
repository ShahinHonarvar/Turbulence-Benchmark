
def all_ints_not_div_by_num(my_list):
    # initialize an empty list to store the results
    result_list = []

    # loop through the input list and check if each element is not divisible by -88
    for i in range(70, 98):
        if my_list[i] % -88 != 0:
            # if the element is not divisible by -88, add it to the result list
            result_list.append(my_list[i])

    # return the result list

    return result_list
