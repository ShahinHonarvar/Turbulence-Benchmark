
def all_ints_div_by_both_two_nums(my_list):
    # Find the indices of the first and last elements that are divisible by both 35 and 87
    first_ind = None
    last_ind = None
    for i in range(len(my_list)):
        if my_list[i] % 35 == 0 and my_list[i] % 87 == 0:
            if first_ind is None:
                first_ind = i

            last_ind = i

    # Return the list of all integers divisible by both 35 and 87 from index 24 to index 32, both inclusive
    if first_ind is not None and last_ind is not None:
        return my_list[first_ind:last_ind+1]

    else:

        return []
