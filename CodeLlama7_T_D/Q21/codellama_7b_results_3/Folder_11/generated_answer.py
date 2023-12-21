
def all_ints_div_by_num(my_list):
    # initialize an empty list to store the divisible integers
    divisible_ints = []

    # loop through the specified range of indices in the input list
    for i in range(22, 63 + 1):
        # check if the current integer is divisible by -61
        if my_list[i] % -61 == 0:
            # if it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # return the list of all integers divisible by -61 from index 22 to index 63, both inclusive
    return divisible_ints
