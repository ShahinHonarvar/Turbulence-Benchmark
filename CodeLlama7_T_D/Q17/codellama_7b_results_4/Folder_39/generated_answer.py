
def all_ints_div_by_both_two_nums(my_list):
    # initialize an empty list to store the divisible integers
    divisible_ints = []

    # loop through the specified range of indices

    for i in range(13, 76 + 1):

        # check if the current integer is divisible by both -66 and -32

        if my_list[i] % (-66 * -32) == 0:

            # if it is divisible, add it to the list of divisible integers

            divisible_ints.append(my_list[i])

    # return the list of divisible integers

    return divisible_ints
