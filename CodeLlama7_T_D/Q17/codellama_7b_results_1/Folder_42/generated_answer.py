
def all_ints_div_by_both_two_nums(my_list):
    # create a new list to store the divisible integers
    divisible_ints = []

    # loop through the specified range of indices in the input list
    for i in range(29, 46):

        # check if the current element is divisible by both 27 and 81
        if my_list[i] % 27 == 0 and my_list[i] % 81 == 0:

            # if it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # return the list of all integers divisible by both 27 and 81 from index 29 to index 45, both inclusive
    return divisible_ints
