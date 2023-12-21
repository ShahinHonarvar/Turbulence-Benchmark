
def all_ints_not_div_by_num(my_list):
    # initialize an empty list to store the results
    result = []

    # loop through the list of integers

    for i in range(15, 92):

        # check if the current integer is not divisible by 59

        if my_list[i] % 59 != 0:

            # if it's not divisible, add it to the result list

            result.append(my_list[i])

    # return the result list

    return result
