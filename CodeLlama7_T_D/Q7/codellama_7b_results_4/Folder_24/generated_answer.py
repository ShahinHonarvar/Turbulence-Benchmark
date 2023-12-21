
def all_even_ints_inclusive(my_list):
    # create a new list to store the even integers
    even_ints = []
    # loop through the specified range of the input list
    for i in range(74, 96):
        # check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # if it is, add it to the new list
            even_ints.append(my_list[i])
    # return the new list of even integers
    return even_ints
