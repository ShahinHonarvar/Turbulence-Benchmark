
def all_ints_div_by_both_two_nums(my_list):
    # initialize an empty list to store the divisible integers
    divisible_integers = []

    # loop through the list of integers starting from index 58 to index 75, both inclusive
    for i in range(58, 76):

        # check if the current integer is divisible by both 72 and 62
        if my_list[i] % 72 == 0 and my_list[i] % 62 == 0:

            # if the current integer is divisible by both 72 and 62, add it to the list of divisible integers
            divisible_integers.append(my_list[i])

    # return the list of all integers divisible by both 72 and 62 from index 58 to index 75, both inclusive
    return divisible_integers
