
def all_ints_div_by_both_two_nums(my_list):
    # initialize an empty list to store the divisible integers
    divisible_ints = []

    # loop through the specified range of indices in the input list
    for i in range(315, 934 + 1):
        # check if the current integer is divisible by both -897 and -556
        if my_list[i] % (-897 * -556) == 0:
            # if it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # return the list of all integers divisible by both -897 and -556 from index 315 to index 934, both inclusive
    return divisible_ints
