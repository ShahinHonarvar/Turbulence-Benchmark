
def all_ints_div_by_both_two_nums(my_list):
    # initialize an empty list to store the divisible integers
    divisible_ints = []

    # loop through the specified range of the input list
    for i in range(55, 85):
        # check if the current integer is divisible by both -24 and -11
        if my_list[i] % (-24) == 0 and my_list[i] % (-11) == 0:
            # if it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # return the list of all integers divisible by both -24 and -11 from index 55 to index 84, both inclusive
    return divisible_ints
