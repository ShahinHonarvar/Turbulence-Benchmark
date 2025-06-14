
def all_ints_div_by_both_two_nums(my_list):
    # initialize an empty list to store the divisible integers
    divisible_ints = []

    # loop through the specified range of the list
    for i in range(29, 46):
        # check if the current integer is divisible by both 27 and 81
        if my_list[i] % 27 == 0 and my_list[i] % 81 == 0:
            # if it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # return the list of all integers divisible by both 27 and 81 from index 29 to index 45, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    return divisible_ints
