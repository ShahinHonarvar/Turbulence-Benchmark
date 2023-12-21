
def all_even_ints_inclusive(my_list):
    # create a new list to store the even integers
    even_ints = []
    # loop through the list of integers from index 37 to index 76, both inclusive
    for i in range(37, 77):
        # if the current element is even, append it to the new list
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    # return the new list of even integers
    return even_ints
