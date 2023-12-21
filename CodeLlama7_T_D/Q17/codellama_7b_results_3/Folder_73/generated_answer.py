
def all_ints_div_by_both_two_nums(my_list):
    # initialize an empty list to store the divisible integers
    divisible_ints = []

    # loop through the specified range of indices in my_list
    for i in range(81, 87):
        # check if the integer at index i is divisible by both -33 and -62
        if (my_list[i] % -33 == 0) and (my_list[i] % -62 == 0)):
            # if it is, append it to the list of divisible integers
            divisible_ints.append(my_list[i])

    return divisible_ints
