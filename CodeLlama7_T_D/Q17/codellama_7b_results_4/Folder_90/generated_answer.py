
def all_ints_div_by_both_two_nums(my_list):
    # initialize an empty list to store the divisible integers
    div_ints = []

    # loop through the list of integers starting from index 138 to index 424, both inclusive
    for i in range(138, 425):
        # check if the current integer is divisible by both -863 and -329
        if my_list[i] % (-863 * -329) == 0:
            # if it is divisible, add it to the list of divisible integers
            div_ints.append(my_list[i])

    # return the list of all integers divisible by both -863 and -329 from index 138 to index 424, both inclusive
    return div_ints
