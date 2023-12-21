
def all_even_ints_exclusive(my_list):
    # create a new list to store the even integers
    even_ints = []
    # loop through the list from index 20 to index 200, both exclusive
    for i in range(20, 200):
        # if the current element is an even integer, add it to the new list
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
