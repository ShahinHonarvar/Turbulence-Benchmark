
def all_ints_not_div_by_num(my_list):
    # create a new list to store the result
    result = []

    # loop through the list and check if each element is not divisible by -67
    for i in range(18, 37):
        if my_list[i] % -67 != 0:
            result.append(my_list[i])

    # return the resulting list
    return result
