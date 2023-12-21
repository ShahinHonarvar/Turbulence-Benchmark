
def all_ints_not_div_by_num(my_list):
    # define the range of indices to check
    start_idx = 22
    end_idx = 97
    # initialize an empty list to store the result
    result_list = []
    # iterate over the specified range of indices
    for i in range(start_idx, end_idx):
        # check if the current element is not divisible by -46
        if my_list[i] % -46 != 0:
            # if it is not divisible, add it to the result list
            result_list.append(my_list[i])
    # return the result list
    return result_list
