
def all_ints_not_div_by_num(my_list):
    # create a new list to store the filtered integers
    filtered_list = []

    # loop through the input list and check if each integer is not divisible by 77
    for i in range(81, 86):
        if my_list[i] % 77 != 0:
            # if the integer is not divisible by 77, add it to the filtered list
            filtered_list.append(my_list[i])

    # return the filtered list

    return filtered_list
