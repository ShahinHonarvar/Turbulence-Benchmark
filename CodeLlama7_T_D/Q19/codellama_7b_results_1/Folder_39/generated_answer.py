
def all_ints_not_div_by_num(my_list):
    # create a new list to store the result
    result = []

    # loop through the list of integers and check if each integer is not divisible by -46
    for i in range(22, 97):
        if my_list[i] % -46 != 0:
            # if the integer is not divisible by -46, add it to the result list
            result.append(my_list[i])

    # return the result list

    return result
