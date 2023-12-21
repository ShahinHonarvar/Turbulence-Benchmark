
def all_even_ints_exclusive(my_list):
    # create a new list to store the even integers
    even_ints = []

    # loop through the list from index 41 to index 69 (both exclusive)
    for i in range(41, 70):

        # check if the current element is an even integer
        if my_list[i] % 2 == 0:

            # if it is, add it to the list of even integers
            even_ints.append(my_list[i])

    # return the list of all even integers from index 41 to index 69 (both exclusive)
    return even_ints
