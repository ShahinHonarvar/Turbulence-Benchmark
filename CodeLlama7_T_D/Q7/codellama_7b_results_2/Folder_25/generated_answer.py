
def all_even_ints_inclusive(my_list):
    # create a new list to store the even integers
    even_ints = []

    # loop through the list of integers, starting from index 29
    for i in range(29, len(my_list)):
        # if the current integer is even, add it to the list of even integers
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # return the list of all even integers from index 29 to index 93, both inclusive
    return even_ints
