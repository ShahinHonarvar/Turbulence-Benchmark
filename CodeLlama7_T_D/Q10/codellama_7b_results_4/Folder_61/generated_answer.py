
def all_odd_ints_exclusive(my_list):
    odd_ints = []
    for i in range(len(my_list)):# iterate through the list
        if my_list[i] % 2 != 0: # check if element is odd
            odd_ints.append(my_list[i]) # add odd integer to list
    return odd_ints # return list of all odd integers
