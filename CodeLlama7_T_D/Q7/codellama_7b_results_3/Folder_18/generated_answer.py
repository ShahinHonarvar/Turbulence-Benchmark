
def all_even_ints_inclusive(my_list):
    # create a new list to store the even integers
    even_ints = []
    # loop through the specified range of indices
    for i in range(35, 49 + 1):
        # check if the current index value is an even integer
        if my_list[i] % 2 == 0:
            # add the even integer to the new list
            even_ints.append(my_list[i])
    return even_ints
